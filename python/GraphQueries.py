import datetime
from FileOperations import *
from GraphStatistics import *


def match_suggestion(person_knows, person_lives, person_studies, person_works, node_id, interests, hops, age_diff, limit):

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
        final.append((candidate[1], score))

    return final


def filter_gender(node_id, person_knows, recommendations):

    gender = (person_knows.lookup_node(node_id)).attributes["gender"]

    for temp_node in recommendations:
        temp_gender = (person_knows.lookup_node(temp_node)).attributes["gender"]
        if gender == temp_gender:
            recommendations.remove(temp_node)

    return recommendations


def filter_age(node_id, person_knows, recommendations, age_diff):

    age1 = (person_knows.lookup_node(node_id)).attributes["age"]
    birthdate1 = datetime.datetime.strptime(age1, '%Y-%m-%d')

    for temp_node in recommendations:
        age2 = (person_knows.lookup_node(temp_node)).attributes["age"]
        birthdate2 = datetime.datetime.strptime(age2, '%Y-%m-%d')
        age_difference = abs((birthdate1 - birthdate2).days)/365
        if age_difference > age_diff:
            recommendations.remove(temp_node)

    return recommendations


def filter_places(node_id, person_lives, person_studies, person_works, recommendations):

    person_studies_r = create_reverse_graph_from_file("person_studyAt_organisation.csv")
    person_works_r = create_reverse_graph_from_file("person_workAt_organisation.csv")
    person_lives_r = create_reverse_graph_from_file("person_isLocatedIn_place.csv")

    bfs_gen = person_lives.bfs_graph(node_id)          #oi perioxes poy menei o node
    city_living = []
    for city in bfs_gen:
        city_living.append(city[0])

    bfs_gen = person_studies.bfs_graph(node_id)        #ta universities toy node
    uni_studying = []
    for uni in bfs_gen:
        uni_studying.append(uni[0])

    bfs_gen = person_works.bfs_graph(node_id)         #ta workplaces toy node
    work_places = []
    for job in bfs_gen:
        work_places.append(job[0])

    all_in_nodes_uni = []                          #oloi poy spoydazoyn se kapoio ap ta universities toy node
    for uni in uni_studying:
        bfs_gen = person_studies_r.bfs_graph(uni)
        for student in bfs_gen:
            all_in_nodes_uni.append(student[0])

    all_in_jobs = []
    for job in work_places:
        bfs_gen = person_works_r.bfs_graph(job)
        for employee in bfs_gen:
            all_in_jobs.append(employee[0])

    all_in_cities = []
    for city in city_living:
        bfs_gen = person_lives_r.bfs_graph(city)
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
    interests = b_node.intersts
    for pers in recommendations:
        temp_node = person_knows.lookup_node(pers)
        common = 0
        for interest in temp_node.interests:
            if interest in interests:
                common += 1
        if common > num_of_interests:
            final.append((common, pers))

    return final


def get_top_stalkers(person_knows, limit, likes_threshold, centrality_mode, stalkers_list):
    # get persons with more than <likes_threshold> likes on another persons post
    stalkers = get_stalkers(likes_threshold, person_knows)
    scored_stalkers = rank_stalkers(stalkers, person_knows, centrality_mode)
    for i in range(limit):
        stalkers_list.append((scored_stalkers[i][1], scored_stalkers[i][0]))


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

    return results


def rank_stalkers(stalkers, person_knows, centrality_mode):
    scored_stalkers = []
    if centrality_mode == 1:
        for stalker in stalkers:
            score = closeness_centrality(person_knows, stalker)
            scored_stalkers.append((score, stalker))
    elif centrality_mode == 2:
        # compute score of stalkers with betweenness centrality
        scored_stalkers.append((1, 1))

    scored_stalkers.sort()
    return scored_stalkers
