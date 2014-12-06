

def match_suggestion(person_knows, person_lives, person_studies, person_works, node, interests, hops, age_diff, limit):

    if node not in graph.dictionary:
        print 'Node ' + node + ' is not in the graph'
        return -1


    bfs_generator = person_knows.graph_bfs(node)
    recommendations = []

    for result in bfs_generator:
        if result[1] < hops:
            recommendations.append(result[0])

    recommendations = filter_age(node, person_knows, recommendations, age_diff)
    recommendations = filter_places(node, person_lives, person_studies, person_works, recommendations)





def filter_age(node, person_knows, recommendations, age_diff):

    age = (person_knows.lookup_node(node)).attributes[age]

    for temp_node in recommendations:
        temp_age = (person_knows.lookup_node(temp_node)).attributes[age]
        if abs(age - temp_age) > age_diff:
            recommendations.remove(temp_node)

    return recommendations

def filter_places(node, person_lives, person_studies, person_works, recommendations):

    bfs_gen = person_lives.bfs_graph(node)          #oi perioxes poy menei o node
    city_living = []
    for city in bfs_gen:
        city_living.append(city[0])

    bfs_gen = person_studies.bfs_graph(node)        #ta universities toy node
    uni_studying = []
    for uni in bfs_gen:
        uni_studying.append(uni[0])

    bfs_gen = person_works.bfs_graph(node)         #ta workplaces toy node
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