import pyperclip
import matplotlib.pyplot as plt
import numpy as np

'''
Notes:
Max Courses per semester: 18 hours, can petition up to 21 hours

BIOE Requirements:
Major Reqs: 97-99 Hours
Degree Reqs: 131 Hours
Advanced Reqs: 48 Hours at 300 Level or Above

DSCI Requirements:
Minor Reqs: 27-30 Hours
Advanced Reqs: 18-20 Hours at 300 Level or Above

ENGI Requirements:
Minor Reqs: 18 Hours

General Requirements:
Complete 1 Hour LPAP
Distribution I: 9 Hours
Distribution II: 9 Hours
Distribution III: 9 Hours

'''
#Course Name
bsbe = []
mbe = []

#General CODE
bsbe_code = []
mbe_code = []

#Y/N
core = []
#CODE with number
course_code = []
mbe_course_code = []
#9,3,2,etc.
hours = []
mbe_hours = []
#1, 2, 3, or 0
dist = []
#Course Description
mbe_desc = []

bsbe.append('INTRODUCTORY BIOLOGY I')
bsbe_code.append('BIOS')
course_code.append('BIOS 201')
hours.append(3)
core.append('Y')
dist.append(3)

bsbe.append('CELL BIOLOGY')
bsbe_code.append('BIOS')
course_code.append('BIOS 341')
hours.append(3)
core.append('Y')
dist.append(3)

bsbe.append('GENERAL CHEMISTRY I')
bsbe_code.append('CHEM')
course_code.append('CHEM 121')
hours.append(3)
core.append('Y')
dist.append(3)

bsbe.append('GENERAL CHEMISTRY LABORATORY I')
bsbe_code.append('CHEM')
course_code.append('CHEM 123')
hours.append(1)
core.append('Y')
dist.append(0)

bsbe.append('GENERAL CHEMISTRY II')
bsbe_code.append('CHEM')
course_code.append('CHEM 122')
hours.append(3)
core.append('Y')
dist.append(3)

bsbe.append('GENERAL CHEMISTRY LABORATORY II')
bsbe_code.append('CHEM')
course_code.append('CHEM 124')
hours.append(1)
core.append('Y')
dist.append(0)

bsbe.append('ORGANIC CHEMISTRY I')
bsbe_code.append('CHEM')
course_code.append('CHEM 211')
hours.append(3)
core.append('Y')
dist.append(3)

bsbe.append('INTRODUCTION TO ENGINEERING COMPUTATION')
bsbe_code.append('CAAM')
course_code.append('CAAM 210')
hours.append(3)
core.append('Y')
dist.append(3)

bsbe.append('ELECTRONIC MEASUREMENT SYSTEMS')
bsbe_code.append('ELEC')
course_code.append('ELEC 243')
hours.append(4)
core.append('Y')
dist.append(3)

bsbe.append('SINGLE VARIABLE CALCULUS I')
bsbe_code.append('MATH')
course_code.append('MATH 101')
hours.append(3)
core.append('Y')
dist.append(3)

bsbe.append('SINGLE VARIABLE CALCULUS II')
bsbe_code.append('MATH')
course_code.append('MATH 102')
hours.append(3)
core.append('Y')
dist.append(3)

bsbe.append('ORDINARY DIFFERENTIAL EQUATIONS AND LINEAR ALGEBRA')
bsbe_code.append('MATH')
course_code.append('MATH 211')
hours.append(3)
core.append('Y')
dist.append(3)

bsbe.append('MULTIVARIABLE CALCULUS')
bsbe_code.append('MATH')
course_code.append('MATH 212')
hours.append(3)
core.append('Y')
dist.append(3)

bsbe.append('ENGINEERING MECHANICS')
bsbe_code.append('MECH')
course_code.append('MECH 211')
hours.append(3)
core.append('Y')
dist.append(0)

bsbe.append('HONORS MECHANICS (WITH LAB)')
bsbe_code.append('PHYS')
course_code.append('PHYS 111')
hours.append(4)
core.append('Y')
dist.append(3)

bsbe.append('HONORS ELECTRICITY \& MAGNETISM (WITH LAB)')
bsbe_code.append('PHYS')
course_code.append('PHYS 112')
hours.append(4)
core.append('Y')
dist.append(3)

bsbe.append('BIOENGINEERING FUNDAMENTALS')
bsbe_code.append('BIOE')
course_code.append('BIOE 252')
hours.append(4)
core.append('Y')
dist.append(0)

bsbe.append('SYSTEMS PHYSIOLOGY LAB MODULE ')
bsbe_code.append('BIOE')
course_code.append('BIOE 320')
hours.append(1)
core.append('Y')
dist.append(0)

bsbe.append('FUNDAMENTALS OF SYSTEMS PHYSIOLOGY')
bsbe_code.append('BIOE')
course_code.append('BIOE 322')
hours.append(3)
core.append('Y')
dist.append(3)

bsbe.append('BIOREACTION ENGINEERING')
bsbe_code.append('BIOE')
course_code.append('BIOE 330')
hours.append(3)
core.append('Y')
dist.append(0)

bsbe.append('BIOENGINEERING THERMODYNAMICS')
bsbe_code.append('BIOE')
course_code.append('BIOE 332')
hours.append(3)
core.append('Y')
dist.append(0)

bsbe.append('LABORATORY IN TISSUE CULTURE')
bsbe_code.append('BIOE')
course_code.append('BIOE 342')
hours.append(1)
core.append('Y')
dist.append(0)

bsbe.append('BIOMATERIALS')
bsbe_code.append('BIOE')
course_code.append('BIOE 370')
hours.append(3)
core.append('Y')
dist.append(0)

bsbe.append('BIOMECHANICS')
bsbe_code.append('BIOE')
course_code.append('BIOE 372')
hours.append(3)
core.append('Y')
dist.append(0)

bsbe.append('BIOMEDICAL INSTRUMENTATION LAB')
bsbe_code.append('BIOE')
course_code.append('BIOE 385')
hours.append(1)
core.append('Y')
dist.append(0)

bsbe.append('BIOMEDICAL ENGINEERING INSTRUMENTATION')
bsbe_code.append('BIOE')
course_code.append('BIOE 383')
hours.append(3)
core.append('Y')
dist.append(0)

bsbe.append('NUMERICAL METHODS')
bsbe_code.append('BIOE')
course_code.append('BIOE 391')
hours.append(3)
core.append('Y')
dist.append(0)

bsbe.append('TRANSPORT PHENOMENA IN BIOENGINEERING')
bsbe_code.append('CHBE')
course_code.append('CHBE 420')
hours.append(3)
core.append('Y')
dist.append(0)

bsbe.append('STATISTICS FOR BIOENGINEERING')
bsbe_code.append('STAT')
course_code.append('STAT 440')
hours.append(1)
core.append('Y')
dist.append(0)

bsbe.append('BIOENGINEERING DESIGN I')
bsbe_code.append('BIOE')
course_code.append('BIOE 451')
hours.append(4)
core.append('Y')
dist.append(0)

bsbe.append('BIOENGINEERING DESIGN II')
bsbe_code.append('BIOE')
course_code.append('BIOE 452')
hours.append(3)
core.append('Y')
dist.append(0)

bsbe.append('COMPUTATIONAL MODELING LAB')
bsbe_code.append('BIOE')
course_code.append('BIOE 446')
hours.append(2)
core.append('Y')
dist.append(0)

bsbe.append('DIGITAL DESIGN \& VISUALIZATION')
bsbe_code.append('BIOE')
course_code.append('BIOE 447')
hours.append(2)
core.append('Y')
dist.append(0)

bsbe.append('MICROCONTROLLER APPLICATONS')
bsbe_code.append('BIOE')
course_code.append('BIOE 421')
hours.append(3)
core.append('N')
dist.append(0)

bsbe.append('IMPLEMENTATION OF DIGITAL SYSTEMS')
bsbe_code.append('ELEC')
course_code.append('ELEC 327')
hours.append(3)
core.append('N')
dist.append(0)

bsbe.append('DIGITAL LOGIC DESIGN')
bsbe_code.append('ELEC')
course_code.append('ELEC 220')
hours.append(3)
core.append('N')
dist.append(0)

bsbe.append('INTRODUCTION TO NEUROENGINEERING: MEASURING AND MANIPULATING NEURAL ACTIVITY')
bsbe_code.append('BIOE')
course_code.append('BIOE 380')
hours.append(3)
core.append('N')
dist.append(0)

bsbe.append('FUNDAMENTALS OF MEDICAL IMAGING I')
bsbe_code.append('BIOE')
course_code.append('BIOE 485')
hours.append(3)
core.append('N')
dist.append(0)

bsbe.append('MATRIX ANALYSIS')
bsbe_code.append('CAAM')
course_code.append('CAAM 335')
hours.append(3)
core.append('N')
dist.append(0)

bsbe.append('CELLULAR ENGINEERING')
bsbe_code.append('BIOE')
course_code.append('BIOE 321')
hours.append(3)
core.append('N')
dist.append(0)

bsbe.append('INTRODUCTION TO ENERGY-EFFICIENT MECHATRONICS')
bsbe_code.append('MECH')
course_code.append('MECH 435')
hours.append(3)
core.append('N')
dist.append(0)

bsbe.append('DESIGN OF MECHATRONIC SYSTEMS')
bsbe_code.append('MECH')
course_code.append('MECH 488')
hours.append(3)
core.append('N')
dist.append(0)

bsbe.append('ADVANCES IN BIONANOTECHNOLOGY')
bsbe_code.append('BIOE')
course_code.append('BIOE 403')
hours.append(3)
core.append('N')
dist.append(0)

bsbe.append('NEUROMUSCULOSKELETAL MODELING AND SIMULATION')
bsbe_code.append('MECH')
course_code.append('MECH 497')
hours.append(3)
core.append('N')
dist.append(0)

bsbe.append('BIOMATERIALS APPLICATIONS')
bsbe_code.append('BIOE')
course_code.append('BIOE 431')
hours.append(3)
core.append('N')
dist.append(0)

bsbe.append('SENSORY NEUROENGINEERING')
bsbe_code.append('BIOE')
course_code.append('BIOE 492')
hours.append(3)
core.append('N')
dist.append(0)
# bsbe_desc.append('This course will explore how bioengineering techniques and principles are applied to understand and model sensory systems, with a focus on the auditory, vestibular, and visual systems. The interaction between the electrical, mechanical and optical aspects of these systems, and ways to modulate these interactions, will be explored. The course will also cover the design of current auditory, visual and somato-sensory neuroprosthetics (i.e. cochlear- implants, retinal implants and brain-machine interfaces), as well as emerging technologies for neural stimulation.')


bsbe.append('ENGINEERING DESIGN AND COMMUNICATION')
bsbe_code.append('FWIS')
course_code.append('FWIS 188')
hours.append(3)
core.append('Y')
dist.append(1)

bsbe.append('SECOND YEAR ARABIC 1')
bsbe_code.append('ARAB')
course_code.append('ARAB 263')
hours.append(3)
core.append('N')
dist.append(1)

bsbe.append('SECOND YEAR ARABIC 2')
bsbe_code.append('ARAB')
course_code.append('ARAB 264')
hours.append(3)
core.append('N')
dist.append(1)

bsbe.append('INTRO TO PSYCHOLOGY')
bsbe_code.append('PSYCH')
course_code.append('PSYCH 101')
hours.append(3)
core.append('N')
dist.append(2)

bsbe.append('DATA, ETHICS, AND SOCIETY')
bsbe_code.append('DSCI')
course_code.append('DSCI 305')
hours.append(3)
core.append('Y')
dist.append(2)

bsbe.append('PROBABILITY AND STATISTICS FOR DATA SCIENCE')
bsbe_code.append('STAT')
course_code.append('STAT 315')
hours.append(4)
core.append('Y')
dist.append(3)

bsbe.append('INTRODUCTION TO DATA SCIENCE TOOLS AND MODELS')
bsbe_code.append('DSCI')
course_code.append('DSCI 302')
hours.append(3)
core.append('Y')
dist.append(0)

bsbe.append('MACHINE LEARNING FOR DATA SCIENCE')
bsbe_code.append('DSCI')
course_code.append('DSCI 303')
hours.append(3)
core.append('Y')
dist.append(0)

bsbe.append('INTRODUCTION TO EFFECTIVE DATA VISUALIZATION')
bsbe_code.append('DSCI')
course_code.append('DSCI 304')
hours.append(3)
core.append('Y')
dist.append(0)

bsbe.append('APPLIED MACHINE LEARNING AND DATA SCIENCE PROJECTS')
bsbe_code.append('COMP')
course_code.append('COMP 449')
hours.append(3)
core.append('Y')
dist.append(0)

bsbe.append('FINANCIAL MANAGEMENT')
bsbe_code.append('BUSI')
course_code.append('BUSI 343')
core.append('N')
hours.append(3)
dist.append(2)

bsbe.append('LPAP')
bsbe_code.append('LPAP')
course_code.append('LPAP 100')
core.append('Y')
hours.append(1)
dist.append(0)

bsbe.append('ENTREPRENEURIAL STRATEGY')
bsbe_code.append('BUSI')
course_code.append('BUSI 463')
core.append('N')
hours.append(3)
dist.append(0)

set_bsbe_codes = set(bsbe_code)
bsbe_code_counts = []
txport = [] #course, code

for code in set_bsbe_codes:
    counter = 0
    for course in bsbe_code:
        if code == course:
            counter += 1
        else:
            pass
        # print(f'Code: {code}, Counter: {counter}')
    bsbe_code_counts.append([code, counter])

print(bsbe_code_counts)

bsbe_code_counts_np = []
labels = []
for pair in range(len(bsbe_code_counts)):
    bsbe_code_counts_np.append(bsbe_code_counts[pair][1])
    labels.append(bsbe_code_counts[pair][0])
    

bsbe_course_list = ''

for pair in bsbe:
    bsbe_course_list+=pair.title()+'\n'

for pair in range(len(bsbe)):
    txport.append([bsbe_code[pair], bsbe[pair]])

bsbe_code_counts_np = np.array(bsbe_code_counts_np)
print(bsbe_course_list)
plt.pie(bsbe_code_counts_np, labels=labels)
plt.figtext(0.1, 0.05, bsbe_course_list, fontsize='small')
plt.show()

mbe.append('HEALTHCARE INNOVATION AND ENTREPRENEURSHIP')
mbe_code.append('BIOE')
mbe_course_code.append('BIOE 527')
mbe_hours.append(3)
mbe_desc.append('This course is designed for healthcare entrepreneurs who want to build innovative medical technologies. During the course, students will learn how to identify customers, key stakeholders, and the market opportunity for a clinical need; apply design thinking, including low-fidelity prototyping, to quickly test and iterate on a concept; assess regulatory, reimbursement, and clinical trial requirements; identify key assumptions and develop a business model; create a financial model based on business model assumptions; determine capital requirements and funding sources for their venture; understand and evaluate term sheets; create a pitch presentation for investors.')

mbe.append('HEALTHCARE INNOVATION AND ENTREPRENEURSHIP LAB')
mbe_code.append('BIOE')
mbe_course_code.append('BIOE 529')
mbe_hours.append(3)
mbe_desc.append('In this follow-on experiential Lab course, students work on refining and completing the plan for the venture they created in Health Innovation and Entrepreneurship. Teams receive guidance and Mentoring from faculty and mentors to develop the next steps of their business. The Lab takes place in the Liu Idea Lab for Innovation and Entrepreneurship, a purpose built state-of-the-art incubator and co-working space on the Rice campus.')

mbe.append('MEDICAL ENGINEERING AND DESIGN LAB')
mbe_code.append('BIOE')
mbe_course_code.append('BIOE 528')
mbe_hours.append(3)
mbe_desc.append('In this studio-based lab, students apply technical engineering and prototyping skills to medical design projects. Participants are taught and apply a range of topics including engineering design processes, medical materials, biocompatibility, design for manufacturing, rapid prototyping, medical equipment, sterility, manufacturing techniques, and quality system implementation.')

mbe.append('MEDICAL ENGINEERING AND DESIGN LAB 2')
mbe_code.append('BIOE')
mbe_course_code.append('BIOE 530')
mbe_hours.append(3)
mbe_desc.append('In this studio-based lab, students apply technical engineering and prototyping skills to medical design projects. Participants are taught and apply a range of topics including engineering design processes, medical materials, biocompatibility, design for manufacturing, rapid prototyping, medical equipment, sterility, manufacturing techniques, and quality system implementation. This course is intended for only those students in Bioengineering.')

mbe.append('MEDICAL INNOVATION INDUSTRY SEMINAR')
mbe_code.append('BIOE')
mbe_course_code.append('BIOE 627')
mbe_hours.append(1.5)
mbe_desc.append('This course exposes participants to the wide variety of career paths in the medical technology industry including large to mid sized companies, consulting, biotech, pharma, diagnostics, hospital administration and more through guest lectures, case studies, and informational interviews. Additional topics include: Resume and LinkedIn refinement, Job Application Process, Interview Skills, Delivering Oral Presentations')

mbe.append('ROLES OF PHYSICIANS, SCIENTISTS, ENGINEERS AND MBA\'S IN HIGH-TECH STARTUPS')
mbe_code.append('MGMT')
mbe_course_code.append('MGMT 633')
mbe_hours.append(1.5)
mbe_desc.append('This pragmatic course combines core lectures on entrepreneurship with special guest presentations by notable life science entrepreneurs. It explores the roles that physicians, scientists, engineers, and MBA\'s play in biotech, medical device, and healthcare companies, as well as major trends in Angel and Venture Capital Financings of Startups. Lectures on entrepreneurial team building, leadership and career planning are included.')

mbe.append('GRADUATE INDEPENDENT STUDY')
mbe_code.append('BIOE')
mbe_course_code.append('BIOE 506')
mbe_hours.append(6)
mbe_desc.append('Independent investigation of a specific topic in modern bioengineering research under the direction of a faculty member.')

# mbe.append('WORKPLACE COMMUNICATION FOR PROFESSIONAL MASTER\'S STUDENTS IN ENGINEERING')
# mbe_code.append('ENGI')
# mbe_course_code.append('ENGI 501')
# mbe_hours.append(3)
# mbe_desc.append('This course will equip students with strategies to communicate more successfully on the job. Students will improve their written, oral, visual and interpersonal communication skills through formal and informal assignments, in-class activities, practice, and feedback.')

# mbe.append('TECHNICAL AND MANAGERIAL COMMUNICATIONS')
# mbe_code.append('ENGI')
# mbe_course_code.append('ENGI 510')
# mbe_hours.append(3)
# mbe_desc.append('In this communications course designed for Engineering Professional Masters (EPM) students, the approach will be experiential and interactive, with in-class exercises, analyses, and presentations. The focus will be on your practicing and refining the oral, written, and interpersonal skills you will need in your professional career. You should be prepared to participate in class. If you are a non-native speaker, you should be very proficient speaking and writing English and you should not take this course in your first semester at Rice. Preference will be given to EPM students.')

# \\\\\\
# mbe.append('LEADING TEAMS AND INNOVATION')
# mbe_code.append('ENGI')
# mbe_course_code.append('ENGI 515')
# mbe_hours.append(3)
# mbe_desc.append('Students learn the principles of engineering leadership, strategies for launching and leading engineering teams, and methods for utilizing creativity and innovation in engineering environments. Learning methods include case studies, simulations, group projects, and interactions with industry professionals. Graduate students are required to complete an additional paper focusing on leadership development.')
# \\\\\\

# mbe.append('ETHICS AND ENGINEERING LEADERSHIP')
# mbe_code.append('ENGI')
# mbe_course_code.append('ENGI 529')
# mbe_hours.append(3)
# mbe_desc.append('Seminar introduces students to a framework for discussing and making ethical engineering and professional decisions. Using case studies and exercises, students will look at their own profession and its Engineering Code of Ethics as well as at the issues and risks they may face as managers and executives. Graduate students will do an extra paper.')

# mbe.append('PROFESSIONAL COMMUNICATION FOR ENGINEERING LEADERS')
# mbe_code.append('ENGI')
# mbe_course_code.append('ENGI 542')
# mbe_hours.append(3)
# mbe_desc.append('Students develop communication skills starting with critical thinking about communication strategy and how to best organize a message for different audiences. They will build skills in oral presentations, writing, data visualization, and interpersonal communication to communicate clearly and confidently in a variety of professional situations.')

mbe.append('MANAGEMENT FOR SCIENCE AND ENGINEERING')
mbe_code.append('ENGI')
mbe_course_code.append('ENGI 610')
mbe_hours.append(3)
mbe_desc.append('This course is for graduate and undergraduate students who want to understand the basics of management in new and/or small technology-based businesses and is particularly relevant to students who are interested in careers in technology or entrepreneurial ventures. NSCI 610/ENGI 610 is team taught to provide insight into how technology oriented firms manage people, projects, accounting, marketing, strategy, intellectual property, organizations and entrepreneurship.')

# mbe.append('LEADERSHIP COACHING FOR ENGINEERS')
# mbe_code.append('ENGI')
# mbe_course_code.append('ENGI 615')
# mbe_hours.append(3)
# mbe_desc.append('Leadership coaching is a professional skill that leaders use to enhance another person\'s ability to achieve their goals. Students will learn how to lead others in their own professional development through the use of coaching. This course emphasizes experiential learning and some graduates will be selected to become coaches to Rice engineering undergraduates.')

mbe.append('APPLIED STATISTICS FOR BIOENGINEERING AND BIOTECHNOLOGY')
mbe_code.append('BIOE')
mbe_course_code.append('BIOE 539')
mbe_hours.append(3)
mbe_desc.append('Course will cover fundamentals of probability and statistics with emphasis on application to biomedical problems and experimental design. Recommended for students pursuing careers in medicine or biotechnology.')

mbe.append('MACHINE LEARNING AND SIGNAL PROCESSING FOR NEURO ENGINEERING')
mbe_code.append('BIOE')
mbe_course_code.append('BIOE 548')
mbe_hours.append(3)
mbe_desc.append('The activity of a complex network of billions of interconnected neurons underlies our ability to sense, represent and store the details of experienced life, and enables us to interact with our environment and other organisms. Modern neuroscience techniques enable us to access this activity, and thus to begin to understand the processes whereby individual neurons enable complex behaviors. In order to increase this understanding and to design biomedical systems which might therapeutically interact with neural circuits, advanced statistical signal processing and machine learning approaches are required. This class will cover a range of techniques and their application to basic neuroscience and neural interfaces. Topics include latent variable models, point processes, Bayesian inference, dimensionality reduction, dynamical systems, and spectral analysis. Neuroscience applications include modeling neural firing rates, spike sorting, decoding, characterization of neural systems, and field potential analysis.')

# mbe.append('SENSORY NEUROENGINEERING')
# mbe_code.append('BIOE')
# mbe_course_code.append('BIOE 592')
# mbe_hours.append(3)
# mbe_desc.append('This course will explore how bioengineering techniques and principles are applied to understand and model sensory systems, with a focus on the auditory, vestibular, and visual systems. The interaction between the electrical, mechanical and optical aspects of these systems, and ways to modulate these interactions, will be explored. The course will also cover the design of current auditory, visual and somato-sensory neuroprosthetics (i.e. cochlear- implants, retinal implants and brain-machine interfaces), as well as emerging technologies for neural stimulation.')

# ********************
mbe.append('BUILDING LIFE SCIENCES, BIOMEDICAL AND BIOTECHNOLOGY STARTUPS')
mbe_code.append('BIOE')
mbe_course_code.append('BIOE 593')
mbe_hours.append(3)
mbe_desc.append('This semester-long course aims to provide entrepreneurial students with a hands-on experience in building a high-tech company based on novel biomedical technologies being developed at Rice University and in the Texas Medical Center. Students will form teams of 2-4, and identify a promising biomedical technology, perform intellectual property landscape analysis, identify a minimum viable product, build a business plan, construct 1 year and 5 year financial projections, conduct voice of customer interviews, and present a fundraising ``pitch.\'\' Students are expected to spend 8-10 hours per week outside the classroom to complete tasks assigned during lectures, and will summarize their findings every 2 weeks in a 7-minute presentation.')
# ********************

# ********************
mbe.append('ENGINEERING DRUG DELIVERY SYSTEMS')
mbe_code.append('BIOE')
mbe_course_code.append('BIOE 515')
mbe_hours.append(3)
mbe_desc.append('This course will focus on the application of innovative engineering approaches to enhance drug efficacy and/or reduce toxicity. Topics of emphasis include, but are not limited to, routes of administration, bioavailability, biodistribution, pharmacokinetics, pharmacodynamics, therapeutic drug windows, patient compliance, immunogenicity, the foreign body reaction, and solubility enhancement. A wide array of device types will be discussed, such as biodegradable microspheres, self-assembled lipid nanoparticles, microneedles, and osmotic pumps. Students will be expected to quantitatively evaluate drug release from complex devices and determine drug distribution and clearance using multi-compartment models. An additional project will be required of graduate level students.')
# ********************

mbe.append('NANOBIOENGINEERING AND NANOMEDICINE')
mbe_code.append('BIOE')
mbe_course_code.append('BIOE 525')
mbe_hours.append(3)
mbe_desc.append('Covers broad range of topics in nanobioengineering and nanomedicine, including synthesis characterization and fractionalization of nanomaterials and nanostructures, nanoparticle-based molecular imaging probes, nanocarriers, for drug/gene delivery, and nanomachines for gene editing and regulation. Examples will be given to illustrate the applications of nanobioengineering and nanomedicine.')

mbe.append('ADVANCES IN GENOME EDITING AND ENGINEERING')
mbe_code.append('BIOE')
mbe_course_code.append('BIOE 526')
mbe_hours.append(3)
mbe_desc.append('This is a course for graduate students who are interested in learning the emerging field of precision genome editing and its applications in biology and medicine. This is a lecture course consisting of classes that meet weekly for 3 hours; instruction is delivered both in a lecture setting and through projects.')

# ********************
mbe.append('FRONTIERS IN IMMUNOENGINEERING')
mbe_code.append('BIOE')
mbe_course_code.append('BIOE 536')
mbe_hours.append(3)
mbe_desc.append('This course will introduce immunology concepts from an engineering perspective and covers various immune responses including to pathogens, self, allergens, cancer, and biomaterials. Using principles of engineering we will perform an in-depth analysis of these responses and the latest advances on the development of novel therapeutics. Topics include systems immunology, nanotechnology, hydrogels, biomaterials, vaccines, cancer immunotherapy, autoimmunity, tissue engineering, stem cells, viruses, and the microbiome.')
# ********************

# mbe.append('NANO-NEUROTECHNOLOGY')
# mbe_code.append('BIOE')
# mbe_course_code.append('BIOE 680')
# mbe_hours.append(3)
# mbe_desc.append('This course will review current nanofabricated technologies for measuring, manipulating, and controlling neural activity. The course will be based on reviewing current academic literature and topics will include nano-electronic, -photonic, -mechanical, and -fluidic neural devices.')

# mbe.append('BIOMATERIALS APPLICATIONS')
# mbe_code.append('BIOE')
# mbe_course_code.append('BIOE 631')
# mbe_hours.append(3)
# mbe_desc.append('Emphasis will be placed on issues regarding the design, synthesis, evaluation, regulation and clinical translation of biomaterials for specific applications. An overview of significant biomaterials engineering applications will be given, including topics such as ophthalmologic, orthopedic, cardiovascular and drug delivery applications, with attention to specific case studies. Regulatory issues concerning biomaterial will also be addressed. Assignments for this class will include frequent readings of the scientific literature with occasional homework questions, one midterm and cumulative final, a group project, a seminar report and individual presentations. In addition, graduate students in BIOE 631 will have additional exam problems and an additional research paper.')

mbe.append('3D PRINTING AND ADDITIVE MANUFACTURING: THEORY AND APPLICATIONS')
mbe_code.append('MSNE')
mbe_course_code.append('MSNE 513')
mbe_hours.append(3)
mbe_desc.append('Basic principles and applications of additive manufacturing (AM), Various AM processes. Materials science such as polymers, metals, ceramics, composites, and bio-materials for AM. Selection of material and process for design applications such as structures, electronics, biomedical, and consumer products. Hands-on experience and analysis from digital data to physical objects.')

set_mbe_codes = set(mbe_code)
mbe_code_counts = []

for code in set_mbe_codes:
    counter = 0
    for course in mbe_code:
        if code == course:
            counter += 1
        else:
            pass
        # print(f'Code: {code}, Counter: {counter}')
    mbe_code_counts.append([code, counter])

print(mbe_code_counts)

mbe_code_counts_np = []
labels = []
for pair in range(len(mbe_code_counts)):
    mbe_code_counts_np.append(mbe_code_counts[pair][1])
    labels.append(mbe_code_counts[pair][0])


mbe_course_list = ''
for pair in mbe:
    mbe_course_list+=pair.title()+'\n'

mbe_code_counts_np = np.array(mbe_code_counts_np)
print(mbe_code_counts_np)

mbe_txport = [] #course, code

for pair in range(len(mbe)):
    mbe_txport.append([mbe_code[pair], mbe[pair]])

tot_hours_mbe = int(sum(mbe_hours))
max_hours = 24*2

print(mbe_txport)
print(max_hours - tot_hours_mbe)

mbe_texfile = ''
mbe_400 = 0
mbe_500 = 0
mbe_600 = 0

for pair in range(len(mbe)):
    mbe_texfile += '\t%s & %s & \\multicolumn{4}{p{6cm}|}{%s} & %d & 0\\\\\n' %(mbe[pair], mbe_course_code[pair], mbe_desc[pair], mbe_hours[pair])
    if int(mbe_course_code[pair].split()[1]) >= 500 and int(mbe_course_code[pair].split()[1]) < 600:
        mbe_500 += mbe_hours[pair]
    elif int(mbe_course_code[pair].split()[1]) >= 600 and int(mbe_course_code[pair].split()[1]) < 700:
        mbe_600 += mbe_hours[pair]
    elif int(mbe_course_code[pair].split()[1]) >= 400 and int(mbe_course_code[pair].split()[1]) < 500:
        mbe_400 += mbe_hours[pair]

print(mbe_texfile)
pyperclip.copy(mbe_texfile)

print(f'You have taken {tot_hours_mbe} hours')
print(f'You have {mbe_400} hours in level 400')
print(f'You have {mbe_500} hours in level 500')
print(f'You have {mbe_600} hours in level 600')

plt.pie(mbe_code_counts_np, labels=labels)
plt.figtext(0.1, 0.3, mbe_course_list)
plt.show()





























print(txport)
print(len(txport))

bioe = [i for i in txport if i[0]=='BIOE' or i[0]=='ELEC' or i[0]=='MECH' or i[0]=='CAAM' or i[0]=='PHYS'
        or i[0]=='CHEM' or i[0]=='MATH' or i[0]=='BIOS' or i[0]=='CHBE']
dsci = [i for i in txport if i[0]=='DSCI' or i[0]=='COMP' or i[0]=='STAT']
oth = [i for i in txport if i[0]=='FWIS' or i[0]=='BUSI' or i[0]=='PSYCH' or i[0]=='ARAB' or i[0]=='FCM']

texfile = ''
used = []
for j in range(len(oth)):
    texfile += f'\t{bioe[j][0]}: {bioe[j][1]} & '
    texfile += f'{dsci[j][0]}: {dsci[j][1]} & '
    texfile += f'{oth[j][0]}: {oth[j][1]} \\\\\n'
    used.append(bioe[j])
    used.append(dsci[j])
    used.append(oth[j])

for j in range(len(dsci)):
    if bioe[j] not in used:
        texfile += f'\t{bioe[j][0]}: {bioe[j][1]} & '
        texfile += f'{dsci[j][0]}: {dsci[j][1]} & '
        texfile += 'N/A\\\\\n'
        used.append(bioe[j])
    else:
        pass

for k in bioe:
    if k not in used:
        texfile += f'\t{k[0]}: {k[1]} & '
        texfile += 'N/A & '
        texfile += 'N/A\\\\\n'

# print(texfile)


d1 = 0
d2 = 0
d3 = 0
adv = 0
h1 = 0
h2 = 0
h3 = 0
h4 = 0

for i in range(len(bsbe)):
    if dist[i] == 1:
        d1+=hours[i]
    elif dist[i] == 2:
        d2+=hours[i]
    elif dist[i] == 3:
        d3+=hours[i]
    else:
        pass

    if hours[i] == 1:
        h1+=1
    elif hours[i] == 2:
        h2+=1
    elif hours[i] == 3:
        h3+=1
    elif hours[i] == 4:
        h4+=1
    else:
        pass

l100 = 0
l200 = 0
l300 = 0
l400 = 0
l500 = 0

for i in range(len(course_code)):
    if int(course_code[i].split(' ')[1]) >= 300:
        adv+=hours[i]
    else:
        pass
    if int(course_code[i].split(' ')[1]) < 200:
        l100+=hours[i]
    elif int(course_code[i].split(' ')[1]) >= 200 and int(course_code[i].split(' ')[1]) < 300:
        l200+=hours[i]
    elif int(course_code[i].split(' ')[1]) >= 300 and int(course_code[i].split(' ')[1]) < 400:
        l300+=hours[i]
    elif int(course_code[i].split(' ')[1]) >= 400 and int(course_code[i].split(' ')[1]) < 500:
        l400+=hours[i]
    elif int(course_code[i].split(' ')[1]) >= 500 and int(course_code[i].split(' ')[1]) < 600:
        l500+=hours[i]
    else:
        l500+=hours[i]

total_hours = sum(hours)

texfile = ''

for i in range(len(bsbe)):
    texfile+=f'\t{bsbe[i]} & {course_code[i]} & $\square$ & $\square$ & $\square$ & $\square$ & {hours[i]} & {dist[i]}\\\\\n'
    print(f'{course_code[i]} {bsbe[i]}: {hours[i]} Hour(s)')

print('\nSUMMARY:\n')
print(f'{d1} Distribution I hours\n{d2} Distribution II hours\n{d3} Distribution III hours\n')
print(f'You have {adv} hours in Level 300 courses or higher\n')
print(f'You have {h1} courses worth 1 hour')
print(f'You have {h2} courses worth 2 hours')
print(f'You have {h3} courses worth 3 hours')
print(f'You have {h4} courses worth 4 hours')
print(f'You will take {total_hours} hours total')

print('You can have maximum of 18 hours in first year\nYou can petition for up to 24 hours per semester after first year')
vanilla = 18*2*4
petition = (18*2) + (24*2*3)
print(f'Maximum possible hours without petition: {vanilla}')
print(f'Maximum hours with max petitions: {petition}')
diff_vanilla = vanilla - total_hours
diff_pet = petition - total_hours
print(f'You still have room for {diff_vanilla} hours without petition')
print(f'Or you can still have room for {diff_pet} hours with petition')
print(f'Level 100: {l100}\nLevel 200: {l200}\nLevel 300: {l300}\nLevel 400: {l400}\nLevel 500: {l500}')
print(l100+l200+l300+l400+l500)
print(len(course_code))
tmp_math = 18*2 + 24*3*2
print(sum(hours))
print(tmp_math)
pyperclip.copy(texfile)