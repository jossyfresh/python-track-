if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks = list(student_marks.get(query_name))
    sum =0
    for x in marks:
        sum=sum+x
    avarage = (sum/3)
    print(format(avarage,".2f"))
