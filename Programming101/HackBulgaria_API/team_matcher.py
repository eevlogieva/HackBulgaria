import requests
import random


def main():
    print("Hello, you can use one of the following commands:"
            + "\n" + "list_courses - this lists all the courses that are available now."
            + "\n" + "match_teams <course_id>, <team_size>, <group_time>")
    hack_api = requests.get("https://hackbulgaria.com/api/students/", verify=False)
    students = hack_api.json()
    hash_courses = {}
    command = input("enter command: ")
    lst = command.split(" ")
    while lst[0] != "finnish":
        if lst[0] == "list_courses":
            list_courses(students, hash_courses)
        if lst[0] == "match_teams":
            match_teams(students, hash_courses, lst[1], lst[2], lst[3])
        command = input("enter command: ")
        lst = command.split(" ")


def list_courses(students, hash_courses):
    print("Here are the cources:")
    #print(hack_api.text)
    courses = set()
    for student in students:
        for course in student["courses"]:
            courses.add(course["name"])
    for index, course in enumerate(courses):
        hash_courses[int(index + 1)] = course
    print(hash_courses)


def match_teams(students, hash_courses, course_id, team_size, group_time):
    people_here = []
    for student in students:
        for course in student["courses"]:
            if course["name"] == hash_courses[int(course_id)] and course["group"] == int(group_time) and student["available"]:
                people_here.append(student["name"])
    random.shuffle(people_here)
    while len(people_here) > int(team_size):
        for i in range(int(team_size)):
            print(people_here[0])
            people_here.pop(0)
        print("=============")
    length = len(people_here)
    for i in range(length):
        print(people_here[0])
        people_here.pop(0)

if __name__ == '__main__':
    main()
