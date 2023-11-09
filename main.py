import csv


def get_category(path):
    """docstring
    returns the list of names of all categories
    """
    with open(path, 'r') as f:
        line = f.readline()
        category_list=list(map(str,line.split(',')))
        category_list[len(category_list)-1] = category_list[len(category_list)-1].strip()
        
        return category_list

def get_fullStudentdata(path):
    """ docstring
    read data from the csv file

    intput:
        path of csv file
    
    argument used in function:
        category: name of features that create the most impact on the Stress of a Student
        
    output:
        datadict_list: list that contains dictionaries
            dictionary contain the level of each features for a single student
    """
    with open(path, 'r') as f:
        FLAG =True
        datadict_list = []
        for line in f.readlines():
            if FLAG: FLAG = False #ignore first line
            else:
                category = get_category(path)
                temp_dict={}
                temp_list = list(map(int, line.split(',')))
                for idx in range(len(category)):
                    temp_dict[category[idx]] = temp_list[idx] # get rid of blank space

                datadict_list.append(temp_dict)
        
        return datadict_list

def get_avg(category, dataset_list):
    """docstring

    caculates the average level of a specific factor

    input:
    category
    dataset_list

    output:
    average level
    """
    sum_val = 0
    for student in dataset_list: sum_val += student[category]

    return round(sum_val/len(dataset_list),3)

def get_maxVal(category, dataset_list):
    """docstring

    caculates the maximum level of a specific factor

    input:
    category
    dataset_list

    output:
    maximum level
    """
    max_val = -1
    for student in dataset_list: max_val = max(max_val,student[category])

    return max_val

def get_lowerThanAvg(dataset_list, student, category_list):
    """docstring
    figure out the category a specific student has lower level than the average

    input:
    dataset_list
    student
    category_list: category to go through

    output:
    list of category that a specific student has lower level than the average
    """
    ans_list = []
    for category in category_list:
        avg = get_avg(category, dataset_list)
        if student[category] < avg:
            ans_list.append(category)

    return ans_list

def get_higherThanAvg(dataset_list, student, category_list):
    """docstring
    figure out the category a specific student has higher or equal level than the average

    input:
    dataset_list
    student
    category_list: category to go through

    output:
    list of category that a specific student has higher or equal level than the average
    """
    ans_list = []
    for category in category_list:
        avg = get_avg(category, dataset_list)
        if student[category] >= avg:
            ans_list.append(category)

    return ans_list

if __name__ == '__main__':
    f= open("result.txt","w+") # make a text file to store the result
    
    path = 'StressLevelDataset.csv'
    dataset_list = get_fullStudentdata(path)

    positive_factors = ['self_esteem',
                        'sleep_quality',
                        'living_conditions',
                        'safety',
                        'basic_needs',
                        'academic_performance',
                        'teacher_student_relationship',
                        'social_support']
    
    # negative_factors: high level = bad
    # anxiety level isn't included since this will be used as independent variable
    negative_factors = ['depression',
                        'headache',
                        'blood_pressure',
                        'breathing_problem',
                        'noise_level',
                        'study_load',
                        'future_career_concerns',
                        'peer_pressure',
                        'extracurricular_activities',
                        'bullying']
    
    # get average of each level category
    for elem in get_category(path):
        if elem == 'mental_health_history':
            continue
        f.write("Average of {}: {}\n".format(elem, get_avg(elem, dataset_list)))
        f.write("Maximum of {}: {}\n".format(elem, get_maxVal(elem, dataset_list)))
        f.write("-\n")

    f.write("-"*20+"\n")

    f.write("Total number of students: {}\n".format(len(dataset_list)))
    # find # of student who have anxiety level higher than or equal to the average
    # also save their location for the future
    avg_anxiety = get_avg('anxiety_level', dataset_list)
    num_student = 0

    LowThanAvg_list = []
    HighThanAvg_list = []

    for student in dataset_list:
        if student['anxiety_level'] >= avg_anxiety:
            num_student += 1
            LowThanAvg_list.append(student)
        else:
            HighThanAvg_list.append(student)
    f.write("Number of student who have higher anxiety level than the average: {}\n".format(num_student))

    f.write("-"*20+"\n")

    # find the top 10 of the negative categories that the high anxiety level student has higher than the average
    negativeCnt_dict = {}
    for elem in negative_factors:
        negativeCnt_dict[elem] = 0

    for student in HighThanAvg_list:
        for elem in get_higherThanAvg(dataset_list, student, negative_factors):
            negativeCnt_dict[elem] += 1
    
    f.write("Student with high anxiety level also showed high level in these categories:\n")
    cnt = 1
    for category in sorted(negativeCnt_dict.items(), key=lambda x: x[1], reverse=True)[:5]:
        f.write("{}. {} ({})\n".format(cnt, category[0],category[1]))
        cnt += 1
    
    f.write("\n")

    # find the bottom 10 of the positive categories that the high anxiety level student has lower than the average
    positiveCnt_dict = {}
    for elem in positive_factors:
        positiveCnt_dict[elem] = 0

    for student in HighThanAvg_list:
        for elem in get_lowerThanAvg(dataset_list, student, positive_factors):
            positiveCnt_dict[elem] += 1

    f.write("Student with high anxiety level showed low level in these positive categories:\n")
    cnt = 1
    for category in sorted(positiveCnt_dict.items(), key=lambda x: x[1], reverse=True)[:5]:
        f.write("{}. {} ({})\n".format(cnt, category[0],category[1]))
        cnt += 1
    
    f.write("-"*20+"\n")

    # find the top 10 of the positive categories that the low anxiety level student has higher than the average
    positiveCnt_dict = {}
    for elem in positive_factors:
        positiveCnt_dict[elem] = 0

    for student in LowThanAvg_list:
        for elem in get_higherThanAvg(dataset_list, student, positive_factors):
            positiveCnt_dict[elem] += 1
    
    f.write("Student with low anxiety level also showed high level in these positive categories:\n")
    cnt = 1
    for category in sorted(positiveCnt_dict.items(), key=lambda x: x[1], reverse=True)[:5]:
        f.write("{}. {} ({})\n".format(cnt, category[0],category[1]))
        cnt += 1
        
    f.write("\n")


    # find the bottom 10 of the negative categories that the low anxiety level student has lower than the average
    negativeCnt_dict = {}
    for elem in negative_factors:
        negativeCnt_dict[elem] = 0

    for student in LowThanAvg_list:
        for elem in get_lowerThanAvg(dataset_list, student, negative_factors):
            negativeCnt_dict[elem] += 1


    f.write("Student with low anxiety level showed low level in these negative categories:\n")
    cnt = 1
    for category in sorted(negativeCnt_dict.items(), key=lambda x: x[1], reverse=True)[:5]:
        f.write("{}. {} ({})\n".format(cnt, category[0],category[1]))
        cnt += 1
    
    f.close()