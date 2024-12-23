# The Only Todo List You Need

[![Build Status](https://github.com/MasterShifu619/TaskMasterPro/actions/workflows/django.yml/badge.svg)](https://github.com/MasterShifu619/TaskMasterPro/actions/workflows/django.yml)
[![license badge](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/MasterShifu619/TaskMasterPro/blob/main/LICENSE.md)
[![issues badge](https://img.shields.io/github/issues/MasterShifu619/TaskMasterPro)](https://github.com/MasterShifu619/TaskMasterPro/issues)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Django 4.1](https://img.shields.io/badge/django-4.1-blue.svg)](https://docs.djangoproject.com/en/4.1/releases/4.1/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7155415.svg)](https://doi.org/10.5281/zenodo.7155415)
[![GitHub Release](https://img.shields.io/badge/release-v2.0.0-blue)](https://github.com/MasterShifu619/TaskMasterPro/releases/tag/v2.0)
<img src="./coverage.svg">
[![Lint Python](https://github.com/MasterShifu619/TaskMasterPro/actions/workflows/pylint.yml/badge.svg)](https://github.com/MasterShifu619/TaskMasterPro/actions/workflows/pylint.yml)

## TaskMasterPro

TaskMasterPro is a powerful, easy-to-use, and flexible to-do list application designed for busy professionals, students, and anyone looking to stay organized. With a sleek web interface, you can manage your tasks from any device. Access a comprehensive library of templates to get started quickly or customize your list to fit specific needs. With innovative features like shared lists, intelligent task analysis, and real-time alerts, you’ll never miss a deadline again!

### Watch this video to know more about TaskMasterPro 2.0

<img src="img/TaskMasterPro_AnimatedCompressed.gif" width="1200" height="500" />

### Watch below video to know more the original TaskMasterPro

<img src="img/todone-create-list.gif" width="1200" height="500" />

### Watch below video to know more the new and improved TaskMasterPro

(https://www.youtube.com/watch?v=T-Qt4Oh1I98)

## Contents

 * [Why?](#why)
 * [Features](#key-features-last-version)
 * [New Features](#new-features)
 * [Upcoming Features](#upcoming-features)
 * [Quick Start](#quick-start)
 * [Want to contribute?](#want-to-contribute)
 * [License](#license)
 * [Developers](#developers-new-version)

## Why?

We aimed to build something that meets the following criteria:

+ *Purposeful*: An app that fulfills a real need in task management, offering unique tools for productivity.
+ *Scalable*: Designed to work efficiently with a core set of features and expand easily with new functionalities.
+ *Collaborative*: TaskMasterPro's modular structure allows for contributions from multiple developers simultaneously, encouraging teamwork and seamless integration of new features.
+ *Comprehensive*: A project that leverages key Software Engineering practices, from web development and database management to UI/UX design and agile project management.

TaskMasterPro stands out as a functional, efficient to-do app that integrates essential web technologies and practices, all while fostering a productive and collaborative environment.

## Key Features (Last Version)
 * *Register*: Create an account to save and manage your to-do lists across devices.
 * *Login*: Log in securely to access your lists and settings from any device. 
 * *Create, Update, Delete Todo Lists*: Add, modify, or remove lists with a simple interface.
 * *Quickly Create Todo Lists From Templates*: Select from predefined templates to quickly build structured lists.
 * *Custom Templates*: Save time by creating reusable templates tailored to your needs.
 * *Shared List*: Collaborate with others by sharing specific lists for joint task management.
 * *Due Date and Color Tagging*: Assign due dates and color-coded tags to tasks for better organization and urgency recognition.
 * *Tag-based Grouping*: Use customizable tags to group and organize tasks, projects, or lists.
 * *User Productivity Analysis*: Get insights into your productivity trends over time.
 * *Task Analysis*: View detailed analytics on task completion, pending tasks, and more.
 * *Customized Color Tags*: Personalize tags for a more visual, engaging to-do list experience.
 * *Due Date Alerting Mechanism*: Receive timely alerts for upcoming or overdue tasks.
 * *Advanced Scheduler*: Plan tasks with complex scheduling options for improved time management.
 * *Calendar Dashboard*: Visualize tasks and deadlines on a calendar to track deadlines and progress effectively.

## New Features
* *Task Cloning for Repeatable Routines*: Add a "Clone Task" option for quick duplication of recurring tasks with similar settings.
* *Quick Task Ratings*: Prompt users to rate tasks on importance, ease, and satisfaction after completion for personalized insights.
* *Next Task Suggestion*: Recommend the next best task based on urgency, priority, and user preferences.
* *Daily Focus Theme*: Set daily themes (e.g., "Wellness Wednesdays") to help users concentrate on specific task types.
* *Additional Template functionality*: Built on the existing functionality and added a delete template option.
* *UI Redesign*: Redesigned some UI elements of the register page to make things look nicer.


## Upcoming Features

* *Recurring Tasks*: Add functionality for users to set up recurring tasks and reminders for regular activities.
* *Collaboration Tools*: Enhance collaboration features with real-time editing, comments, and file sharing, allowing teams to work together more effectively on shared tasks.
* *Enhancing Task Suggestions*: Incorporate additional inputs, such as estimated completion time and task complexity, to improve the accuracy of the next task suggestions.
  
## Quick Start

 * [Download](https://www.python.org/downloads/release/python-380/) and install Python 3.8.0 or higher.
 * [Install](https://docs.djangoproject.com/en/4.1/topics/install/) Django 4.1.
 * Clone the repository:
    bash
    $ git clone https://github.com/MasterShifu619/TaskMasterPro.git
    
 * Run migrations:
    bash
    $ python manage.py migrate
    
 * Start the app:
    bash
    $ python manage.py runserver 8080
    
 * Open your browser at http://127.0.0.1:8080 to explore TaskMasterPro.

## Features

### Register
<p float="middle">
    <img src="img/Register2.0.0.png" width="500" height="250" />
</p>

### Login, Forget Password
<p float="middle">
    <img src="img/Login2.0.0.png" width="500" height="250" /> 
</p>

### Manage Todo List
<p float="middle">
    <img src="img/Lists2.0.0.png" width="500" height="250" />
</p>

### Cloning
<p float="middle">
    <img src="img/Cloning2.0.0.gif" width="500" height="250" />
</p>

### Rating
<p float="middle">
    <img src="img/Rating2.0.0.gif" width="500" height="250" />
</p>

### Templates
<p float="middle">
    <img src="img/Templates2.0.0.png" width="500" height="250" />
</p>

### User Analytics
<p float="middle">
    <img src="img/UserAnalytics2.0.0.gif" width="500" height="250" />
</p>

### Daily Focus
<p float="middle">
    <img src="img/DailyFocus2.0.0.gif.gif" width="500" height="250" />
</p>

## Want to Contribute?

Interested in contributing? See our [Contributing Guide](CONTRIBUTING.md) for ways to get started.

## License

This project is licensed under the MIT License. For more details, view the [LICENSE](https://github.com/MasterShifu619/TaskMasterPro/blob/release-v2.0.0/LICENSE.md) file.

## Developers (New Version)

<table>
  <tr>
    <td align="center"><a href="https://github.com/MasterShifu619"><img src="https://avatars.githubusercontent.com/u/112150278?v=4" width="100px;" alt=""/><br /><sub><b>Bipin Gowda</b></sub></a></td>
    <td align="center"><a href="https://github.com/IshaDave26"><img src="https://avatars.githubusercontent.com/u/23623764?v=4" width="100px;" alt=""/><br /><sub><b>Isha Dave</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/aj18coep"><img src="https://avatars.githubusercontent.com/u/59056739?v=4" width="100px;" alt=""/><br /><sub><b>Ashlesha Joshi</b></sub></a><br /></td>

  </tr>
</table>

## Developers (Last Version)

* Bipin Gowda (bvgowda@ncsu.edu)
* Isha Dave (idave2@ncsu.edu)
* Ashlesha Joshi (ajoshi28@ncsu.edu)

## :email: Support

For any queries and help, please reach out to us at: bipin.919@gmail.com
