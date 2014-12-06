import datetime

def match_suggestion(person_knows, person_lives, person_studies, person_works, node_id, interests, hops, age_diff, limit):

    if node_id not in graph.dictionary:
        print 'Node ' + node_id + ' is not in the graph'
        return -1


    bfs_generator = person_knows.graph_bfs(node)
    recommendations = []

    for result in bfs_generator:
        if result[1] < hops:
            recommendations.append(result[0])

    recommendations = filter_gender(node_id, person_knows, recommendations)
    recommendations = filter_age(node_id, person_knows, recommendations, age_diff)
    recommendations = filter_places(node_id, person_lives, person_studies, person_works, recommendations)
    final = filter_interests(node_id, person_knows, recommendations, interests)




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
        for empl in bfs_gen:
            all_in_jobs.append(empl[0])

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
            final.append((pers,common))

    return final