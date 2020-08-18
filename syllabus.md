Instructor: A. J. Medford

Email: [ajm@gatech.edu](mailto:ajm@gatech.edu)

Office Hours: [By Appointment](https://app.acuityscheduling.com/schedule.php?owner=18040156&appointmentType=11047919)

Class Hours: W 9:30-10:20am

Office Hours Location: [BlueJeans Office](https://bluejeans.com/4985363696)

Class Room: [BlueJeans](https://bluejeans.com/150999360)

Course Description
==================

About VIP
---------

The Vertically-Integrated Projects (VIP) Program operates in a research
and development context. Undergraduate students that join VIP teams earn
academic credit for their participation in design/discovery efforts that
assist faculty and graduate students with research and development
issues in their areas of expertise.

The teams are:

-   Multidisciplinary - drawing students from all disciplines on campus;

-   Vertically-integrated - maintaining a mix of sophomores through PhD
    students each semester;

-   Long-term - each undergraduate student may participate in a project
    for up to three years and each graduate student may participate for
    the duration of their graduate career.

The continuity, technical depth, and disciplinary breadth of these teams
are intended to: Provide the time and context necessary for students to
learn and practice many different professional skills, make substantial
technical contributions to the project, and experience many different
roles on a large, multidisciplinary design/discovery team. Support
long-term interaction between the graduate and undergraduate students on
the team. The graduate students mentor the undergraduates as they work
on the design/discovery projects embedded in the graduate students’
research. Enable the completion of large-scale design/discovery projects
that are of significant benefit to faculty members’ research programs.

About Big Data and Quantum Mechanics
------------------------------------

This course explores projects at the intersection of computational
chemistry (quantum mechanics) and data science (big data) within the
application domain of surface science and catalysis. The team merges
expertise from computational and physical sciences, and students from
computer science, electrical engineering, industrial & systems
engineering, chemical engineering, chemistry, physics, and materials
science. The VIP course consists of 4 classes of sub-team projects:

-   Training: All new students must complete a “training” project that
    involves the calculation of an adsorption energy using the
    quantum-mechanical technique of density functional theory (DFT), and
    training of a neural network model that can reproduce DFT results.
    The codes for DFT are well-established, but require the use of
    supercomputing resources and must be converged with respect to
    several numerical parameters. The training exercise will introduce
    students to high-performance computing, quantum-mechanical
    simulations, and machine learning packages used for atomic
    simulation data.

-   Data Generation: These projects will utilize DFT calculations
    performed on the PACE supercomputer to generate datasets of
    scientific relevance for problems in surface science and catalysis.
    This may involve the identification of new catalyst materials via
    high-throughput screening, or gaining an in-depth understanding of
    the catalytic behavior of a material based on modeling of various
    intermediate species and reaction pathways. Projects may also
    involve improving the codes used to generate the DFT data, or the
    infrastructure used to collect and organize the resulting data.

-   Machine Learning: These projects will focus on training
    machine-learning models to reproduce the output of DFT calculations.
    In particular, “neural network force-fields” provide a route to
    rapidly predict the energies and forces on atoms based on training
    data gathered from DFT or other atomistic simulation techniques.
    There are established packages like the Atomistic Machine-learning
    Package (AMP) and the Simple-NN package where these models
    are implemented. However, optimizing the architecture and parameters
    of the neural network remains challenging. These projects will work
    with specific datasets and students will try to improve the
    performance of the machine-learning model by
    varying hyper-parameters. 

-   Software Infrastructure: These projects will focus on specific aspects
    of computational tools used or developed by graduate students and 
    advance these tools by implementing new methods, adding documentation,
    or creating new example use cases. Some software tools developed by the
    group or our collaborators include the [ElectroLens](https://medford-group.github.io/ElectroLens/) visualization tool,
    the [SPARC DFT code](https://www.sparc-x.com/), and the [AMPTorch](https://github.com/ulissigroup/amptorch) code for atomistic machine learning.

Course Logistics
================

The course will utilize the following resources for communication and
submission of assignments:

-   Github: All course materials will be posted to Github.

-   Canvas: The course Canvas site will be used for submission of
    assignments and peer grading.

-   Slack: The group Slack channel is the preferred method of
    communication with instructors and graduate students. You are
    responsible for anything that is announced in the `vip`
    Slack channel.

Course Objectives {#course-objectives .unnumbered}
=================

1.  Calculate adsorption energies using the density functional
    theory (DFT)

2.  Converge numerical calculations with respect to input parameters

3.  Submit, manage, and analyze high-performance computing jobs

4.  Utilize machine-learning packages to predict the output of atomistic
    simulations

5.  Work with a team to solve real-world problems at the intersection of
    big data and quantum mechanical simulations

Course Structure
================

The grade will be assigned based on three categories:

-   Documentation: 33.3 %

-   Personal Accomplishments: 33.4 %

-   Teamwork and Interactions: 33.3 %

A grade of 0-5 will be assigned for each category based on the criteria
outlined below. A total grade will be computed based on the weighted
average of the 3 categories which will be converted to letter grades
using the following:

-   A: > 4

-   B: > 3

-   C: < 3

-   D: < 2

You will receive a grade at the midterm and after the end of the course.
The midterm grade is only advisory, and will not factor into the final
calculation.

Documentation
-------------

The documentation grade will be assessed based on bi-weekly updates submitted via Canvas.
The weekly update should include the following components:

- Tasks completed in the prior week
- Discussion of any key challenges or results
- Tasks to be completed in future weeks
- Documentation needed to repeat analysis and access results
- A formal citation of one source (peer-reviewed or permanently archived) that was useful during that week.


Documentation for the bi-weekly updates should be provided as a text file or Word document.
Bi-weekly updates will be peer graded on a scale of 0-5 based on the following criteria (decimal scores are allowed):

-   5: Remarkable progress on tasks, clear description of process and findings, a well-defined plan for the next weeks, and relevant citations (A+)

-   4: Average progress on tasks, some documentation of results/challenges, a reasonable plan for the coming weeks, and relevant citation (A)
Goals are completely achieved (A)

-   3: Some progress on tasks, but documentation and/or plan is lacking detail. A citation is provided, but lacks relevance or appears to be re-used (B)

-   2: Very little progress on tasks, documentation and/or plan is omitted or incomplete. Citation lacks relevance or is omitted (C)

-   1: Clear lack of effort in completing tasks, documentation and plan are omitted or irrelevant. Citation not provided (D)

-   0: No submission

Bi-weekly updates should be compiled into a single document and submitted at the midterm and final. Instructors will review the average score from bi-weekly updates and compare this to the compiled updates to ensure that the peer grading is appropriate, and to ensure that citations are not recycled. Instructors reserve the right to revise the average score up or down if substantial inconsistencies between the score and the criteria above are observed.

Personal Accomplishments
------------------------

Personal accomplishments will be measured by self-defined goals and a
combination of instructor and peer evaluation. Within the **first two weeks**
of the semester students returning to projects will define midterm and
semester goals for their project. Each goal should have a deliverable
that can be unambiguously evaluated as complete or incomplete (computer
code, report, figure, etc.), and each student should submit a
deliverable. Deliverables submitted by team members need not be unique,
but ideally self-defined goals will be individualized, such that each
team member has different deliverables that support a larger team-based
goal.

-   5: Goals are completely achieved and additional progress has been
    made (A+)

-   4: Goals are completely achieved (A)

-   3: Goals are partially achieved (B)

-   2: Some progress has been made, but goals are not achieved (C)

-   1: No substantial progress is made towards goals (D)

Similar to documentation, the accomplishments will be graded by your peers, and confirmed by the
instructor. Importantly, the midterm assessment is only advisory, and
students have an opportunity to **revise goals within 2 weeks of
receiving the midterm assessment**.
The final grade will depend only on the revised goals. This means that
the grade is controlled by two factors: i) ability to plan research and
set realistic targets and ii) ability to achieve goals and deliver on a
plan.

#### New projects:

For new projects (including the training project for new students) the
instructor or sub-team advisor will provide the initial goals. The
training project goals are based on results from prior semesters and are
known to be reasonable; therefore, goals cannot be removed or revised to
be less challenging. However, new project goals may be overambitious and
students are encouraged to revise them at the midterm once they have a
grasp of the long-term goals and scope of the project.

#### Submission and peer review:

The accomplishments will be initially graded by multiple peers and
confirmed by the instructor. The deliverables will be submitted via
Canvas as a .zip file, and a copy of the project goals document should
be included with the submission to aid the reviewers. 
**All submissions should contain a file named "README"** that explains the
accomplishments in the context of the project goals and points the reviewer
to necessary information.
Any external deliverables (e.g. websites, Github, etc.) should be
clearly referenced. The README can also contain any comments, instructions, or
context that may be important for a grader. When grading other students’
assignments you should use the above 1-5 scale and criteria as a
guideline. Only materials included in or referenced in the submission
should be used to assess the criteria (e.g. if a group presents
something in the VIP meeting but does not include it in the submission
then it does not count).

Teamwork and Interaction
------------------------

Teamwork and interaction will be graded based on peer evaluations
conducted through the VIP website and your participation in peer grading.
Note that this can be confusing. **Peer evaluations** occur twice per
semester through the VIP website, while **peer grading** occurs bi-weekly for
documentation and twice per semester for personal achievements.
The **response rate for peer grading and peer evaluations will account 
for 40% of the teamwork and interaction grade.**, while the scores you receive
from your teammates in the peer evaluation will account for the other 60% of
this grade. Note that you **only need to complete peer evals for your sub-team members**,
but **peer grading will be across different subteams** and will be explicitly
assigned.

Meeting Format
--------------

The first weeks will involve an overview of the team, available
projects, and discussion of goals. Subsequent weeks will include
training lectures by graduate students, and/or 10 minute update
presentations by VIP sub-teams. The goal of these presentations is to
present progress and challenges so that the rest of the class can make
suggestions. Updates should be informal and consist of 5 or fewer
slides. The remaining time in the class will be used as a “workshop”
where teams can interact with their sub-team advisor and/or each other
as needed. **If nobody from your group is present when you are scheduled
to present then everyone in the group will lose 1/2 point (out of 5
total) from your “Documentation” grade**. Please let an instructor know
if nobody can make it, and work with other groups to find a time to make
up the presentation.

Schedule 
========

Week 1: Introduction to VIP and projects (Medford)

Week 2: Overview of literature searches (Medford)

Week 3: Intro to Python (Sahoo)

Week 4: Intro to ASE and adsorption energies (Sahoo)

Week 5: PACE and Bash scripting (Sahoo)

Week 6: Density functional theory calculations (Sahoo)

Week 7: Midterm Updates

Week 8: Midterm Updates

Week 9: Atomistic machine learning: theory (Sahoo)

Week 10: Atomistic machine learning: application (Sahoo)

Week 11: Workshop

Week 12: Workshop

Week 13: Final Updates

Week 14: Final Updates

Changes to Syllabus
===================

The schedule and syllabus are subject to change. Given that this is a
research course, changes are to be expected; however, we will do our
best to notify you of any changes and implement them as fairly as
possible.
