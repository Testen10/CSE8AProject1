# CSE8AProject1
## Langauge used
<p><img src="https://img.shields.io/badge/Python-61DAFB?style=flat&logo=React&logoColor=white"/>
version: 3.9.7

## Objective
<p>Analyze student stress factor dataset from Kaggle <a href="https://www.kaggle.com/datasets/rxnach/student-stress-factors-a-comprehensive-analysis", target = "_blank">(link)</a></p>

## Motivating Question
<ul>
  <li>What is the average anxiety level?</li>
  <li>How many students are suffering from high anxiety levels (higher than average level)?</li>
  <li>For those who have high anxiety levels, what are the negative factors that are higher than the average level / positive factors that are lower than the average?</li>
  <li>For those who have low anxiety levels, what are the positive factors that are higher than the average level / negative factors that are lower than the average level?</li>
</ul>


## How this code works
<p>If you run this code, it will geneate a text file 'result.txt' which includes the following analysis:</p>
<blockquote>
<ol>
  <li> Average level of each factor in the dataset</li>
  <li> Maximum level of each factor in the dataset</li>
  <li> Total number of students recorded in the dataset</li>
  <li> Number of students whose anxiety level is higer than the average</li>
  <li> Top 5 negative factors that students with anxiety level higher than the average have higher than the average level</li>
  <li> Top 5 positive factors that students with anxiety level higher than the average have lower than the average level</li>
  <li> Top 5 positive factors that students with anxiety level lower than the average have higher than the average level</li>
  <li> Top 5 negative factors that students with anxiety level lower than the average have lower than the average level</li>
</ol>
</blockquote>

<br> Negative factor refers to the factor where the higher level contributes to higher anxiety level of the student.
<br> List of negative factor:
<blockquote>
<ul>
  <li> depression</li>
  <li> headache</li>
  <li> blood_pressure</li>
  <li> breathing_problem</li>
  <li> noise_level</li>
  <li> study_load</li>
  <li> future_career_concerns</li>
  <li> peer_pressure</li>
  <li> extracurricular_activities</li>
  <li> bullying</li>
</ul>
</blockquote>

<br> Positive factor refers to the factor where the higher level contributes to lower anxiety level of the student.
<br> List of positive factor:
<blockquote>
<ul>
  <li> self_esteem</li>
  <li> sleep_quality</li>
  <li> living_conditions</li>
  <li> safety</li>
  <li> basic_needs</li>
  <li> academic_performance</li>
  <li> teacher_student_relationship</li>
  <li> social_support</li>
</ul>
</blockquote>
