import datetime
from collections import deque
from FileOperations import *
from GraphStatistics import *


def match_suggestion(person_knows, node_id, interests, hops, age_diff, limit):

    person_lives = create_graph_from_file("person_isLocatedIn_place.csv")
    person_studies = create_graph_from_file("person_studyAt_organisation.csv")
    person_works = create_graph_from_file("person_workAt_organisation.csv")

    if node_id not in person_knows.dictionary:
        print 'Node ' + node_id + ' is not in the graph'
        return []

    bfs_generator = person_knows.graph_bfs(node_id)
    recommendations = []

    for result in bfs_generator:
        if result[1] < hops:
            recommendations.append(result[0])

    recommendations = filter_gender(node_id, person_knows, recommendations)
    recommendations = filter_age(node_id, person_knows, recommendations, age_diff)
    recommendations = filter_places(node_id, person_lives, person_studies, person_works, recommendations)
    recommendations = filter_interests(node_id, person_knows, recommendations, interests)

    return score_candidates(node_id, person_knows, recommendations, limit)


def score_candidates(node_id, person_knows, recommendation, limit):
    interest_number = len(person_knows.lookup_node(node_id).interests)
    recommendation.sort()
    final = []
    for candidate in recommendation[:limit]:
        temp_interest_num = len(person_knows.lookup_node(candidate[1]).interests)
        score = float(candidate[0])/float(temp_interest_num + interest_number - candidate[0])
        final.append((score, candidate[1]))
    final.sort()
    super_final = []
    for entry in final:
        super_final.append((entry[1], entry[0]))

    return super_final


def filter_gender(node_id, person_knows, recommendations):

    gender = (person_knows.lookup_node(node_id)).attributes["gender"]

    for temp_node in recommendations:
        temp_gender = (person_knows.lookup_node(temp_node)).attributes["gender"]
        if gender == temp_gender:
            recommendations.remove(temp_node)

    return recommendations


def filter_age(node_id, person_knows, recommendations, age_diff):

    age1 = (person_knows.lookup_node(node_id)).attributes["birthday"]
    birthdate1 = datetime.datetime.strptime(age1, '%Y-%m-%d')

    for temp_node in recommendations:
        age2 = (person_knows.lookup_node(temp_node)).attributes["birthday"]
        birthdate2 = datetime.datetime.strptime(age2, '%Y-%m-%d')
        age_difference = abs((birthdate1 - birthdate2).days)/365
        if age_difference > age_diff:
            recommendations.remove(temp_node)

    return recommendations


def filter_places(node_id, person_lives, person_studies, person_works, recommendations):

    person_studies_r = create_reverse_graph_from_file("person_studyAt_organisation.csv")
    person_works_r = create_reverse_graph_from_file("person_workAt_organisation.csv")
    person_lives_r = create_reverse_graph_from_file("person_isLocatedIn_place.csv")

    bfs_gen = person_lives.graph_bfs(node_id)          #oi perioxes poy menei o node
    city_living = []
    for city in bfs_gen:
        city_living.append(city[0])

    bfs_gen = person_studies.graph_bfs(node_id)        #ta universities toy node
    uni_studying = []
    for uni in bfs_gen:
        uni_studying.append(uni[0])

    bfs_gen = person_works.graph_bfs(node_id)         #ta workplaces toy node
    work_places = []
    for job in bfs_gen:
        work_places.append(job[0])

    all_in_nodes_uni = []                          #oloi poy spoydazoyn se kapoio ap ta universities toy node
    for uni in uni_studying:
        bfs_gen = person_studies_r.graph_bfs(uni)
        for student in bfs_gen:
            all_in_nodes_uni.append(student[0])

    all_in_jobs = []
    for job in work_places:
        bfs_gen = person_works_r.graph_bfs(job)
        for employee in bfs_gen:
            all_in_jobs.append(employee[0])

    all_in_cities = []
    for city in city_living:
        bfs_gen = person_lives_r.graph_bfs(city)
        for citizen in bfs_gen:
            all_in_cities.append(citizen[0])

    for pers in recommendations:
        if (pers not in all_in_cities) and (pers not in all_in_nodes_uni) and (pers not in all_in_jobs):
            recommendations.remove(pers)

    return recommendations


def filter_interests(node_id, person_knows, recommendations, num_of_interests):
    """
    perigrafi
    :param node_id:
    :param person_knows:
    :param recommendations:
    :param num_of_interests:
    :return:
    """
    final = []
    b_node = person_knows.lookup_node(node_id)
    interests = b_node.interests
    for pers in recommendations:
        temp_node = person_knows.lookup_node(pers)
        common = 0
        for interest in temp_node.interests:
            if interest in interests:
                common += 1
        if common >= num_of_interests:
            final.append((common, pers))

    return final


def get_top_stalkers(person_knows, limit, likes_threshold, centrality_mode, stalkers_list):
    # get persons with more than <likes_threshold> likes on another persons post
    stalkers = get_stalkers(likes_threshold, person_knows)
    stalkers_graph = Graph()
    stalkers_graph.fill_from_list(stalkers, person_knows)
    scored_stalkers = rank_stalkers(stalkers_graph, centrality_mode)
    if len(scored_stalkers) < limit:
        limit = len(scored_stalkers)
    for i in range(limit):
        stalkers_list.append((scored_stalkers[i][1], scored_stalkers[i][0]))

    return stalkers_graph


def get_stalkers(likes_threshold, person_knows):
    """
    Create and return a list of people with more than <likes_threshold> likes on someone else they are not friends with
    :param likes_threshold:
    :param person_knows: person knows person graph
    :return: list of requested persons
    """
    person_likes_post_graph = create_graph_from_file("person_likes_post.csv")
    post_has_owner_dict = create_dictionary_from_file("post_hasCreator_person.csv")
    results = []

    for person in person_knows.dictionary:
        bfs_generator = person_likes_post_graph.graph_bfs(person)   # for each person in the graph
        persons_liked = dict()                                      # key: post_owner, value: likes to his posts

        for post_liked in bfs_generator:                            # for each post liked by this person
            post_owner = post_has_owner_dict[post_liked[0]]         # find the owner of the post

            if post_owner in persons_liked:
                likes = persons_liked[post_owner]
                likes += 1
                persons_liked[post_owner] = likes
                if likes >= likes_threshold:                        # stop searching for a person if threshold met
                    if person_knows.reach_node_1(person, post_owner) != 1:  # they are not friends
                        results.append(person)                              # add him to the stalkers
                        break
            else:
                persons_liked[post_owner] = 1
                if 1 >= likes_threshold:                        # stop searching for a person if threshold met
                    if person_knows.reach_node_1(person, post_owner) != 1:  # they are not friends
                        results.append(person)                              # add him to the stalkers
                        break

    return results


def rank_stalkers(stalkers_graph, centrality_mode):
    scored_stalkers = []
    if centrality_mode == 1:            # for closeness centrality
        for stalker in stalkers_graph.dictionary:
            score = closeness_centrality(stalkers_graph, stalker)
            scored_stalkers.append((score, stalker))
    elif centrality_mode == 2:          # for betweenness centrality
        # compute score of stalkers with betweenness centrality
        scored_stalkers.append((1, 1))

    scored_stalkers.sort()
    return scored_stalkers


def find_trends(k, person_knows, women_trends, men_trends):
    womens_graph = Graph()
    mens_graph = Graph()
    women_list = []
    men_list = []
    for person_id in person_knows.dictionary:
        if person_knows.lookup_node(person_id).attributes["gender"] == "male":
            men_list.append(person_id)
        else:
            women_list.append(person_id)

    womens_graph.fill_from_list(women_list, person_knows)
    mens_graph.fill_from_list(men_list, person_knows)

    men_dict = dict()      # key: interest , val: trend size
    women_dict = dict()    # key: interest , val: trend size

    visited = dict()        # key: interest , val: list of visited ids who like this interest

    for man_id in mens_graph.dictionary:
        man_node = mens_graph.lookup_node(man_id)
        for interest in man_node.interests:
            if interest not in visited:
                visited[interest] = [man_id]
            elif man_id not in visited[interest]:
                visited[interest].append(man_id)
            else:
                break

            trend_group = search_trend(mens_graph, man_id, interest, visited[interest])
            trend_group_size = len(trend_group)
            if interest not in men_dict:
                men_dict[interest] = trend_group_size
            elif trend_group_size > men_dict[interest]:
                men_dict[interest] = trend_group_size

            for person_id in trend_group:
                if person_id not in visited[interest]:
                    visited[interest].append(person_id)

    men_trends.extend(top_trends(men_dict, k))
    visited.clear()

    for woman_id in womens_graph.dictionary:
        women_node = womens_graph.lookup_node(woman_id)
        for interest in women_node.interests:
            if interest not in visited:
                visited[interest] = [woman_id]
            elif woman_id not in visited[interest]:
                visited[interest].append(woman_id)
            else:
                break

            trend_group = search_trend(womens_graph, woman_id, interest, visited[interest])
            trend_group_size = len(trend_group)
            if interest not in women_dict:
                women_dict[interest] = trend_group_size
            elif trend_group_size > women_dict[interest]:
                women_dict[interest] = trend_group_size

            for person_id in trend_group:
                if person_id not in visited[interest]:
                    visited[interest].append(person_id)

    women_trends.extend(top_trends(women_dict, k))
    return


def top_trends(dictionary, k):
    trends = []
    for trend in dictionary:
        trends.append((dictionary[trend], trend))
    trends.sort()
    trends.reverse()
    return trends[:k]


def search_trend(graph, start_node_id, trend, already_visited):
    visited_nodes = []
    visited_nodes.extend(already_visited)
    if start_node_id not in visited_nodes:
        visited_nodes.append(start_node_id)
    nodes_to_expand = deque([start_node_id])

    while nodes_to_expand:
        current_node = graph.lookup_node(nodes_to_expand[0])
        current_node_links = current_node.links
        for edge in current_node_links:
            if edge.edge_end not in visited_nodes:
                p_node = graph.lookup_node(edge.edge_end)
                if trend in p_node.interests:
                    visited_nodes.append(edge.edge_end)
                    nodes_to_expand.append(edge.edge_end)
        nodes_to_expand.popleft()

    return visited_nodes


def build_trust_graph(forum_name, person_knows):

    forum_id = -1

    with open("forum.csv", 'r') as input_file:
        first_line = input_file.readline()
        first_line = first_line.rstrip('\n')
        parameters = first_line.split('|')

        for line in input_file:
            line = line.rstrip('\n')
            line = line.split('|')
            if line[1] == forum_name:
                forum_id = int(line[0])
                break

    posts_in_forum = []

    with open("forum_containerOf_post.csv", 'r') as input_file:
        first_line = input_file.readline()
        first_line = first_line.rstrip('\n')
        parameters = first_line.split('|')

        for line in input_file:
            line = line.rstrip('\n')
            line = line.split('|')
            if int(line[0]) == forum_id:
                posts_in_forum.append(int(line[1]))

    person_has_comments = dict()        # key = person_id        val = list of comment ids
    person_has_posts = dict()           # key = person_id        val = list of post ids

    with open("post_hasCreator_person.csv",'r') as input_file:
        first_line = input_file.readline()
        first_line = first_line.rstrip('\n')
        parameters = first_line.split('|')

        for line in input_file:
            line = line.rstrip('\n')
            line = line.split('|')
            if int(line[0]) in posts_in_forum:
                if int(line[1]) in person_has_posts:
                    person_has_posts[int(line[1])].append(int(line[0]))
                else:
                    person_has_posts[int(line[1])] = [int(line[0])]

    with open("comment_hasCreator_person.csv", 'r') as input_file:
        first_line = input_file.readline()
        first_line = first_line.rstrip('\n')
        parameters = first_line.split('|')

        for line in input_file:
            line = line.rstrip('\n')
            line = line.split('|')

    comments_in_forum = []
    comment_of_post = dict()                            # key: comment_id  val: post_id
    with open("comment_replyOf_post.csv", 'r') as input_file:
        first_line = input_file.readline()
        first_line = first_line.rstrip('\n')

        for line in input_file:
            if int(line[1]) in posts_in_forum:
                comments_in_forum.append(int(line[0]))
                comment_of_post[int(line[0])] = int(line[1])

    comments_of_comments = []
    with open("comment_replyOf_comment.csv", 'r') as input_file:
        first_line = input_file.readline()
        first_line = first_line.rstrip('\n')

        for line in input_file:
            if int(line[1]) in comments_in_forum:
                comments_of_comments.append(int(line[0]))
                comment_of_post[int(line[0])] = comment_of_post[int(line[1])]

    comments_in_forum.extend(comments_of_comments)
    comments_of_comments = []

    with open("comment_hasCreator_person.csv", 'r') as input_file:
        first_line = input_file.readline()
        first_line = first_line.rstrip('\n')

        for line in input_file:
            if int(line[0]) in comments_in_forum:
                if int(line[1]) in person_has_comments:
                    person_has_comments[int(line[1])].append(int(line[0]))
                else:
                    person_has_comments[int(line[1])] = [int(line[0])]

    posts_are_liked_by = dict()             # key: post_id          val: list of persons that like the post
    person_likes_posts = dict()             # key: person_id        val: list of posts that person likes
    with open("person_likes_post", 'r') as input_file:
        first_line = input_file.readline()
        first_line = first_line.rstrip('\n')

        for line in input_file:
            if int(line[1]) in posts_in_forum:
                if int(line[1]) in posts_are_liked_by:
                    posts_are_liked_by[int(line[1])].append(int(line[0]))
                else:
                    posts_are_liked_by[int(line[1])] = [int(line[0])]

                if int(line[0]) in person_likes_posts:
                    person_likes_posts[int(line[0])].append(int(line[1]))
                else:
                    person_likes_posts[int(line[0])] = [int(line[1])]

    # person_has_comments = dict()          # key = person_id       val = list of comment ids
    # person_has_posts = dict()             # key = person_id       val = list of post ids
    # posts_are_liked_by = dict()           # key: post_id          val: list of persons that like the post
    # person_likes_posts = dict()           # key: person_id        val: list of posts that person likes
    # comment_of_post = dict()              # key: comment_id       val: post_id

    trust_graph = Graph()
    for person_id in person_knows.dictionary:
        person_node = Node(person_id, [], [])
        trust_graph.insert_node(person_node)

        original_node = person_knows.lookup_node(person_id)
        num_of_total_likes = 0
        if person_id in person_likes_posts:
            num_of_total_likes = len(person_likes_posts[person_id])

        num_of_total_comments = 0
        if person_id in person_has_comments:
            num_of_total_comments = len(person_has_comments[person_id])

        for neighbour_edge in original_node.links:
            neighbour = neighbour_edge.edge_end
            trust_weight = 0
            likes_to_this_neighbour = 0
            for like in person_likes_posts[person_id]:
                if like in person_has_posts[neighbour]:
                    likes_to_this_neighbour += 1

            if likes_to_this_neighbour > 0:
                trust_weight += 0.3 * (float(likes_to_this_neighbour)/float(num_of_total_likes))

            comments_to_this_neighbour = 0
            for comment in person_has_comments[person_id]:
                post_replied = comment_of_post[comment]
                if post_replied in person_has_posts[neighbour]:
                    comments_to_this_neighbour += 1

            if comments_to_this_neighbour > 0:
                trust_weight += 0.7 * (float(comments_to_this_neighbour)/float(num_of_total_comments))

            edge = Edge(neighbour, [("weight", trust_weight)])
            trust_graph.insert_edge(person_id, edge)

    return trust_graph


def estimate_trust(from_node, to_node, trust_graph):
    shortest_paths = trust_graph.dijkstra_shortest_paths_from(from_node, to_node)
    max_trust = 0
    for path in shortest_paths:
        trust_multiplier = 1
        prev_node = trust_graph.lookup_node(from_node)
        for node_id in path:
            for edge in prev_node.links:
                if edge.edge_end == node_id:
                    weight = edge.properties["weight"]
                    trust_multiplier = trust_multiplier * weight

            prev_node = trust_graph.lookup_node(node_id)

        if trust_multiplier > max_trust:
            max_trust = trust_multiplier

    return max_trust