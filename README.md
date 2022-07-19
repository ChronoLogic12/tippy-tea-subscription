# **Tippy** - Tea Subscription

<p align="center">
    <img src="readme-assets/tippy-logo-round.png" width="200px"/>
</p>

[Tippy - live site](https://tippy-tea-subscription.herokuapp.com/)

<p align="center">
    <img src="readme-assets\tippy-responsive.PNG" width="1200px"/>
</p>

_*This site is for training purposes only, the company is fictional and no orders will be charged or receive products.* _

## **About Tippy**

Tippy is a specialist subscription service bringing the greatest tastes from the world of teas to your door. Our experts work with a vast network of growers from around the world to source the best for you each and every month. Whether you're looking to discover something new or simply want the best from your morning cup, explore more of what you love with Tippy.

## **Table of contents**

- [**Tippy** - Tea Subscription](#tippy---tea-subscription)
  - [**About Tippy**](#about-tippy)
  - [**Table of contents**](#table-of-contents)
  - [**UX Design**](#ux-design)
    - [Project Goals](#project-goals)
    - [User Stories](#user-stories)
      - [As a first time user/potential customer -](#as-a-first-time-userpotential-customer--)
      - [As a return user/customer -](#as-a-return-usercustomer--)
      - [As an admin user -](#as-an-admin-user--)
    - [Wireframes](#wireframes)
    - [Design](#design)
  - [Database schema](#database-schema)
  - [Credits](#credits)
    - [Services](#services)
    - [Content](#content)
    - [Media](#media)
    - [Help and Info](#help-and-info)

## **UX Design**

### Project Goals

The goal of this project is to produce an e-commerce website selling monthly specialist tea subscriptions to users. The site will allow users to find information on all services and make/manage their purchases.

### User Stories

#### As a first time user/potential customer -

- Easily understand the sites purpose and learn more about the services offered.
- Easily navigate to all relevant pages.
- Easily find product details and prices to allow me to make and informed decision.
- Create an account to store personal and purchase information.
- Purchase a subscription.
- Sign up for the company newsletter.

#### As a return user/customer -

- Login to my account.
- View and adjust purchase information and maintain user information such as delivery address and payment info.
- View my subscription details.
- Cancel/amend my current subscription.
- Easily find any relevant product/subscription updates.
- Sign up/cancel my subscription to the newsletter.

#### As an admin user -

- Log in to an admin account.
- Send emails to users signed up the the mailing list.
- Add posts to the sites info blog.

For user stories checklist please view the google sheets table [here](https://docs.google.com/spreadsheets/d/1rKYF5s_qeeRhiHWJwbDJQ15gvJIOe2B4bTUiPIVZyoo/edit?usp=sharing).

### Wireframes

Wireframes were created for mobile, tablet and desktop screen sizes with [Figma](https://www.figma.com).

- [Mobile](readme-assets/tippy-wireframes-mobile.png)
- [Tablet](readme-assets/tippy-wireframes-tablet.png)
- [Desktop](readme-assets/tippy-wireframes-desktop.png)

### Design

As tippy is targeted as a specialist and high end service I wanted the site to reflect this with a clean and clear design. I chose to use a fairly soft pallet in shades of green to tie in to the product and give a somewhat premium feel and included a dark raspberry accent/action colour to compliment.

<p align="center">
    <img src="readme-assets/tippy-colour-palette.PNG" width="600px"/>
</p>

## Database schema

Database model created using [dbdiagram.io](https://dbdiagram.io)

<p align="center">
    <img src="readme-assets/database-schema.PNG" width="500px"/>
</p>

The site uses five models as show above:

- user (profile) extends the django user model and stores all required user data.
- subscriptions: represents the plans a user can subscribe to and is extracted from products on stripe using djstripe.
- orders: links user by id to the product they have ordered.
- mailing: holds the email addresses of all people signed up to the mailing list.
- blogs: are created by admin users and display to the user on the blogs page.

## Credits

### Services

- [Materialize](https://materializecss.com/) - layout, interactive components, element styling, text colours and icons.
- [Google fonts](https://fonts.google.com/).
- [Font Awesome](https://fontawesome.com/) - general additional icons.
- [Django](https://www.djangoproject.com/) python framework.
- [Heroku](https://www.heroku.com/) application host.
- [Amazon S3](https://aws.amazon.com) - cloud storage.
- [Gunicorn](https://gunicorn.org/) - wsgi server.
- [MySQL](https://www.sqlite.org/index.html) - database.

### Content

- [Bootstrap](https://getbootstrap.com/) was used to create the collapsing navigation bar and responsive grid layouts
- [Bootstrap Icons](https://icons.getbootstrap.com/) for social media link icons

### Media

- [Cloudinary](https://cloudinary.com/console/c-087b7b36d5737750ed37ab5fb60479/getting-started) CDN was used for cloud based image storage and servicing.
- Images were sourced from [Pexels](https://www.pexels.com/) and can be found in [this collection](https://www.pexels.com/collections/tippy-w5mdqpg/).
- The brand logo and favicon were created my me using [Adobe Ilistrator](https://www.adobe.com/uk/products/illustrator.html).

### Help and Info

- Code Institute learning material - general knowledge.
- Code Institute - 'boutique ado' learning project - specific django knowledge.
- [Stripe documentation](https://stripe.com/docs/billing/quickstart) - checkout app was adapted from code found in the stripe docs billing quick start guid.
- [djstripe](https://dj-stripe.dev/) linking between django and stripe.
- [Codecademy](https://www.codecademy.com/learn) - general knowledge.
- [w3schools](https://www.w3schools.com/) - general knowledge.
- [MND Web Docs](https://developer.mozilla.org/en-US/) - general knowledge.
- [Stack Overflow](https://stackoverflow.com/) - debugging.
- [Django documentation](https://docs.djangoproject.com/en/4.0/)
- [dbdiagram.io](https://dbdiagram.io) used to create database diagram.
- [Youtube tutorial](https://www.youtube.com/watch?v=GBgRMdjAx_c) from [Very Academy](https://www.youtube.com/c/veryacademy) on youtube on testing in django.
- [Github Gist - tommorris](https://gist.github.com/tommorris/cd1048418cccfa346fef) - Create and login as super user in tests.
