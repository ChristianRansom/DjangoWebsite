

skill_list = {
    'Python': 8,
    'Django': 7,
    'Java': 6,
    'Git': 6,
    'HTML': 6,
    'Data Structures': 5,
    'Linux': 5,
    'CSS': 5,
    'Bootstrap': 4,
    'SQL': 4,
    'Android Development': 4,
    'JavaScript': 4,
    'Puppet': 3,
    'AWS': 3,
    'PHP': 3,
}
display_size = 30

skills = []
skills.append("mysql > SELECT Software FROM skills  WHERE Category ='Software' ORDERBY 'mastery';")
skills.append("+" + "-"*display_size + "+" + "-"*display_size + "+")
skills.append("|" + str("skill").center(display_size) + "|" + str("proficiency").center(display_size) + "|")
skills.append("+" + "-"*display_size + "+" + "-"*display_size + "+")

for skill, mastery in skill_list.items():
    skills.append("|" + str(skill).center(display_size) + "|" + str(mastery).center(display_size) + "|")

skills.append("+" + "-"*display_size + "|" + "-"*display_size + "+")
skills.append(str(len(skill_list)) + " rows in set (0.05 sec)")


experience = {
    0: {
        'company': 'Zutek ',
        'title': 'Field Technician',
        'date': 'October 2020 – Present',
        'explanation': {
            '2g83y3s':'Replaced, repaired, and installed technical equipment at retail locations ',
            'm0xe5f6':'Performed the installation of dozens Back-office Servers with Windows 10 by imaging the old PC and migrating the data to the new PC and configuring the new system',
        }
    },
    #1: {
    #    'company': 'Church of the Canyons',
    #    'title': 'College and Career Director',
    #    'date': 'January 2020 – June 2021',
    #    'explanation': {
    #        '0l9e9t8':'Actively mentored and trained college leaders in spiritual formation, evangelism, and outreach methods',
    #        'fe0ka00':'Developed and taught bible study methods weekly',
    #        'z98a229':'Arranged weekly events and fellowship opportunities',
    #    }
    #},
    2: {
        'company': 'TWR (Trans World Radio) ',
        'title': 'Software Developer',
        'date': 'October 2019 – December 2019',
        'explanation': {
            'w2d34fi':'Implemented automated recording and monitoring for a Software Defined Radio client',
            '05445i3':'Created an interface for automated recording with the Python Tornado Web Framework, HTML, JavaScript and SQL',
            'nu212ds':'Set up user authentication and security measures for the web interface',
        }
    },
    3: {
        'company': 'MuttsWorldMine.com ',
        'title': 'Junior Network Administrator',
        'date': 'March 2015 - September 2018',
        'explanation': {
            '446213q':'Managed the deployment and configuration of plugins and files with Puppet.',
            'ky2p4x9':'Led teams on large projects and trained new staff.',
            '258rl34':'Developed several of my own scripts and plugins.',
        }
    },
    4: {
        'company': 'The Masters University ',
        'title': 'Teachers Assistant',
        'date': 'September 2016 - December 2016',
        'explanation': {
            'md1tm7u':'Assisted in grading and tutoring for the Computer and Information Sciences Department',
        }
    },
    5: {
        'company': 'Faith Academy ',
        'title': 'Computer Teacher',
        'date': 'August 2017 - May 2018',
        'explanation': {
            '668ne87':'Taught Kindergarten to Fifth-grade computer classes.',
        }
    },
    6: {
        'company': 'TeachBeyond ',
        'title': 'English Teacher',
        'date': 'May 2017 - July 2017',
        'explanation': {
            '305dz5e':'Taught English lessons to ESL students',
        }
    },
    7: {
        'company': 'Faith Academy ',
        'title': 'Assistant Volleyball Coach',
        'date': 'August 2017 - November 2017',
        'explanation': {
            'oe54q29':'Coached a High School Volleyball team',
        }
    },
    8: {
        'company': 'Bon Appétit Management Company ',
        'title': 'Food Service Worker',
        'date': 'August 2017 - November 2017',
        'explanation': {
            '091v0yh':'Severed in multiple positions, from the dish-room to serving food',
        }
    },
}

projects = {
    0: {
        'name': 'ProductiveProgrammer ',
        'description': 'A personal portfolio and blog',
        'explanation': 'A personal portfolio and blog to show off my projects and interests. Currently a work in progress. ',
        'date': 'October 2021 - Present',
        'link': 'https://productiveprogrammer.me/',
        'image': 'img/sitelogo.png',
        'skills': 'Django, Python, CSS, Bootstrap, html, Digital Ocean, Ubuntu, Postgres',
    },
    1: {
        'name': 'DjangoWebBoards ',
        'description': 'A simple forum website',
        'explanation': 'A Forum and Topic System built with Django created from following this excellent tutorial https://simpleisbetterthancomplex.com/series/beginners-guide/1.11/',
        'date': 'Sep 2019 - Aug 2019',
        'link': 'https://github.com/ChristianRansom/DjangoWebBoards',
        'image': 'img/DjangoWebBoards.png',
        'skills': 'Django, Digital Ocean, CSS, Python, Bootstrap, html',
    },
    2: {
        'name': 'DeepNeuralNetworks ',
        'description': 'Learning Machine Learning',
        'explanation': 'An implementation from scratch of deep neural networks. Allows for the creation of multilayered networks that train through supervised learning and backpropagation.',
        'date': 'Feb 2019 - March 2019',
        'link': 'https://github.com/ChristianRansom/DeepNeuralNetworks',
        'image': 'img/DeepNeuralNetworks.png',
        'skills': 'Python, Neural Networks, Machine Learning',
    },
    3: {
        'name': 'CommandSchedulerPlus ',
        'description': 'A Minecraft plugin that schedules commands',
        'explanation': 'A lightweight plugin that schedules commands across restarts and long periods. This project uses a complex data structure (AVL Tree) to handle the data.',
        'date': 'Oct 2017 - Feb 2018',
        'link': 'https://www.spigotmc.org/resources/commandschedulerplus.51991/',
        'image': 'img/CommandSchedulerPlus.png',
        'skills': 'Java, Algorithms',
    },
    4: {
        'name': 'DodgerBall',
        'description': 'A simple android game',
        'explanation': 'A simple Android game written in Java. This project taught me about the Android Development Environment.',
        'date': 'Jan 2016 - Jun 2016',
        'link': 'https://github.com/ChristianRansom/DodgerBall',
        'image': 'img/DodgerBall.jpg',
        'skills': 'Java, Android Studio, Mobile Development',
    },
    5: {
        'name': 'Snake',
        'description': 'Python Game',
        'explanation': 'A game written in Python using Pygame and TkInter. I was the technical lead on this project and led three other developers to make contributions to the project. ',
        'date': 'Feb 2019 - Jun 2019',
        'link': 'https://www.dropbox.com/s/64623ijxgyl8h2p/Snake.exe?dl=0',
        'image': 'img/SnakeGame.png',
        'skills': 'Python, Project Management, TkInter, Pygame',
    },
    6: {
        'name': 'Job Scraper',
        'description': 'A tool that searches job descriptions',
        'explanation': 'A web crawler that scraped current job listings and analyses the text to find meaningful common words. ',
        'date': 'Feb 2019 - Jun 2019',
        'link': 'https://productiveprogrammer.me/jobscraper/',
        'image': 'img/JobScraper.png',
        'skills': 'Python, Web Crawling, NLTK',
    },
}

