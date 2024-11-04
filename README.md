# Welcome to Dar Tangier

View the live project here

Dar Tangier is a Moroccan-themed, responsive restaurant website with a registration and reservation system for customers to book tables, view the menu, and get in touch with the restaurant. This project was developed as part of the Code Institute's fourth Project Portfolio

# Table of Contents
UX
Agile Development
Features Implemented
Features Left to Implement
Technology Used
Testing
Bugs
Deployment
Resources
Credits and Acknowledgements

# UX

## Goals and Target Audience
Dar Tangier is designed for food enthusiasts, locals, and tourists looking to experience authentic Moroccan cuisine in Munich. The website provides essential features for easy reservation and navigation, suitable for individuals, families, and groups looking to dine at Dar Tangier. 

## Design 
![Screenshot website design](static/assets/images/readme/homepage.png)
The Dar Tangier website embraces a color palette inspired by traditional Moroccan decor, with warm and inviting tones that reflect the ambiance of the restaurant:

- Mahogany and Sand: Rich shades of mahogany and warm sand tones are used as primary colors, 
evoking the earthy warmth and sophistication associated with Moroccan architecture and interior design.
- Accents of Deep Orange and Gold: These accents are used sparingly to highlight call-to-action buttons, enhancing user navigation while fitting the Moroccan theme of hospitality and vibrancy.
- Ivory and Off-White Backgrounds: These tones provide a clean and welcoming background that contrasts beautifully with the deeper colors, ensuring readability and a visually pleasing experience.

This color scheme not only aligns with Moroccan aesthetics but also helps create an inviting, elegant atmosphere for users exploring the restaurant’s offerings and making reservations.

## Database planning
## Initial data structure
![Screenshot database structure](static/assets/images/readme/database.png)
After defining the project goals and the core features I wanted to include, I used Creately to outline the database structure visually. This initial database schema serves as a foundational guide, showcasing the types of data entities and how they relate to one another. The diagram provides a clear layout of the primary tables, including Users, Reservations, and Tables, along with the key relationships between them.

This structure not only assists in understanding data flow and connections but also offers a blueprint for implementing and expanding on the project’s database as development progresse.

## Final data structure
![Screenshot database structure](static/assets/images/readme/final-database.png)
After refining the project and finalizing essential featured, I adjusted the initial database schema to accommodate specific requirements for user management, reservation scheduling, and table availability. Using Creately, I visually outlined the final data structure, focussing on theUser, Table, and Reservation tables, and their relationships. 

## Wireframes
To plan the layout and functionality of each page, wireframes were created with [Balsamiq](https://balsamiq.com/) as visual guides for the user interface.
These wirframes helped outline essential elements and streamline the design process by providing a clear structure for key components like the homepage, menu, reservation system and User profile Management on different screen sizes. 

### Large and medium screens
![Screenshot wireframe homepage large screen](static/assets/images/readme/homepage-large-screen.png)

![Screenshot wireframe menu page large screen](static/assets/images/readme/menu-large-screen.png)

![Screenshot wireframe location page large screen](static/assets/images/readme/location-large-screen.png)

![Screenshot wireframe manage-reservation page large screen](static/assets/images/readme/manage-reservations-large-screen.png)

![Screenshot wireframe profile page large screen](static/assets/images/readme/profile-large-screen.png)


### Small screens

![Screenshot wireframe homepage small screen](static/assets/images/readme/homepage-small-screen.png)

![Screenshot wireframe menu page small screen](static/assets/images/readme/menu-small-screen.png)

![Screenshot wireframe location page small screen](static/assets/images/readme/location-small-screen.png)

![Screenshot wireframe manage-reservation page small screen](static/assets/images/readme/manage-reservations-small-screen.png)

![Screenshot wireframe profile page large screen](static/assets/images/readme/profile-small-screen.png)


# Agile Development
## Overview
This project followed Agile methodology with iterative development cycles, feature prioritization, and task tracking. Development tasks were organized and tracked with GiHub Projects, which ensured the timely delivery of essenntial functionalities. Each spring was dedicated to the development and refinement of specific feature sets, including the homepage design, menu display, user registration, and reservation management. 

I initiated this project with a clear intent to streamline workflow and effectively manage the expected workload. After outlining the major epics, I systematically decomposed them into actionable user stories and smaller tasks. This approach not only enhanced my ability to monitor progress, but also served as a motivational framework to complete the project on schedule. In addition to the user stories, I created distinct issues for each module of the README.md file, further clarifying objectives and ensuring all components were addressed. 

For a comprehensive overview of the project's progress and workflow, please refer to [this Kanban page](https://github.com/users/BilalEssafi1/projects/2)

## User Stories
To kickstart the project, I adopted a user-centric approach. By envisioning myself as a potential user, I identified key features and functionalities that would enhance the website's usability and appeal. I then translated these insights into a set of user stories, prioritizing core features that would provide a solid foundation for the website. 

Each user story was broken down into smaller, actionable tasks, allowing for a structured and efficient development process. As I progressed through the development phase, I tracked my progress and documented any challenges or solutions encountered. This approach ensured a transparent and organized development workflow. 

By prioritizing user needs and following an agile methodology, I aimed to deliver a high-quality website that meets the expectations of both users and stakeholders. 

### List of User Stories
1. [User Story: Home Page](https://github.com/BilalEssafi1/dar-tangier-project/issues/15)
2. [User Story: Admin Panel](https://github.com/BilalEssafi1/dar-tangier-project/issues/22)
3. [User Story: Sign-Up for Account](https://github.com/BilalEssafi1/dar-tangier-project/issues/16)
4. [User Story: Sign-In to Account](https://github.com/BilalEssafi1/dar-tangier-project/issues/17)
5. [User Story: Manage Reservations](https://github.com/BilalEssafi1/dar-tangier-project/issues/18)
6. [User Story: Delete Account](https://github.com/BilalEssafi1/dar-tangier-project/issues/19)
7. [User Story: Forgot Password](https://github.com/BilalEssafi1/dar-tangier-project/issues/20)
8. [User Story: Manage User Information](https://github.com/BilalEssafi1/dar-tangier-project/issues/21)


# Features Implemented

## Homepage
- Navbar: User-friendly navigation bar is present on all pages and it adapts to the user's authentication status (logged in or not.) Logged-in users have access to profile and reservation management features. 
- Home Page: Displays a visually appealing hero image, well-organized content like Introduction, Featured Dishes and Contact Form. 
- Footer: Displays essential information such as contact details, social media links, and opening hours. 

## User Registration and Profile
- Account Creation: Users can register to make reservations.
- Profile Management: Users can update profile details and change passwords.
- Account Deletion: Option to delete account with confirmation prompts.

## Reservations
- Booking Form: Allows users to select date, time, and guest count.
- Reservation Success and Management: Users receive confirmation and can manage reservations via their profile.
- Table Availability: System checks for available tables and confirms reservation.

## Menu
- Dish Categories: Starters, main courses, and desserts with descriptions and pricing.

## Location
- Map Integration: Uses Google Maps to show the restaurant’s location.

## Responsive Design
The website is mobile-friendly and responsive across all devices, optimized with Bootstrap for consistent styling.

## Future Feature ideas
- Enhanced Reservation Notifications: Email reminders or SMS for confirmed reservations.
- Menu Management for Admin: Allow admin users to update the menu dynamically.
- Table Availability Display: Real-time display of available tables before booking.


# Technology Used
- Frontend: HTML, CSS, JavaScript, Bootstrap
- Backend: Django, Python
- Database: PostgreSQL (configured for production via DATABASE_URL)
- Deployment: Deployed on Heroku, with dj_database_url for database handling.
- Other: Google Maps API, Font Awesome for icons, and Crispy Forms for Django form styling.

# Testing

# Deployment

# Ressources

# Credits and Acknowledgement