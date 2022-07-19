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
  - [Features](#features)
    - [Navigation](#navigation)
    - [Footer](#footer)
    - [Messages - toasts](#messages---toasts)
    - [Home](#home)
    - [Subscriptions](#subscriptions)
    - [About Us](#about-us)
    - [Blog](#blog)
    - [Profile](#profile)
    - [Mailing](#mailing)
    - [Auth](#auth)
      - [Log In](#log-in)
      - [Sign Out](#sign-out)
      - [Register](#register)
    - [Error Pages](#error-pages)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [Deploying to Heroku](#deploying-to-heroku)
    - [Configuring Stripe](#configuring-stripe)
    - [Configuring Gmail](#configuring-gmail)
    - [Configuring AWS S3](#configuring-aws-s3)
    - [Cloning and running locally](#cloning-and-running-locally)
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

The site uses django-allauth pages for user management. All pages have been styled to match the rest of the website.

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

## Features

### Navigation

The sites navigation section is located at the top of all pages. This section contains page navigation controls and is adaptive to screen size and where the current user is logged in. The navigation elements will also highlight depending on the current page.

<p align="center">
    <img src="readme-assets\navbar-desktop.PNG" width="1200px"/>
</p>
<p align="center">
    <img src="readme-assets\navbar-desktop-logged-out.PNG" width="1200px"/>
</p>
For smaller screen sizes the navbar is collapsible and is accessed byt a burger icon in the top left of the screen.
<p align="center">
    <img src="readme-assets\navbar-mobile.PNG" width="1200px"/>
</p>
<p align="center">
    <img src="readme-assets\navbar-sidenav.PNG" width="100px"/>
</p>

1. When logged in the page links are as follows: Subscriptions - About Us - Blog - Profile - Log Out.
2. When logged out the page links are as follows: Subscriptions - About Us - Blog - Register - Log In.

### Footer

The footer is located at the bottom of all pages and contains links to social media pages, sign up page for newsletter/mailing list and a message informing the user that this site is fictional.

<p align="center">
    <img src="readme-assets\footer.PNG" width="1200px"/>
</p>

### Messages - toasts

This site uses djangos messages framework to provide users with helpful feedback at multiple points through their journey in the form of toasts.

<p align="center">
    <img src="readme-assets\messages-toast.PNG" width="150px"/>
</p>

### Home

The homepage consists of two main sections; the first contains a small description of what tippy is and it's service, it also contains a prominent call to action button which will take the user to the subscriptions page. at the bottom of this section is a chevron button which when clicked scrolls the page to the next section.

<p align="center">
    <img src="readme-assets\home-main.PNG" width="1200px"/>
</p>

The 'How It Works' section contains three cards detailing the journey a customer will go through in order to start a subscription as well as some more details about the service.

<p align="center">
    <img src="readme-assets\how-it-works.PNG" width="1200px"/>
</p>

### Subscriptions

The subscription page contains cards for each plan that can be subscribed to detailing: name, image, description and price for each as well as a button which will take the user to the checkout page to complete the purchase of that subscription.

<p align="center">
    <img src="readme-assets\subscriptions.PNG" width="1200px"/>
</p>

### About Us

The about us page is for users who want to learn a little more about the company. It contains two cards each containing details on the companies ideal and philosophies as well as the work they are doing.

<p align="center">
    <img src="readme-assets\about-us.PNG" width="1200px"/>
</p>

### Blog

The blog page contains blog post updates created by admins. each post contains a title, image, body text and the author.

<p align="center">
    <img src="readme-assets\blog.PNG" width="200px"/>
</p>

When logged in as an admin this page has additional features. There is a button at the top of the page which will take the user to a form to create a new post, as well as edit and delete controls for each existing blog. The delete button will bring up a box to confirm/cancel the deletion. Selecting confirm will remove the blog post from the database.

<p align="center">
    <img src="readme-assets\blog-admin-controls.PNG" width="200px"/>
</p>

The add new blog page contains a form with fields for all required blog information. Selecting add will add this information to the database, cancel will return the user to the blogs page.

<p align="center">
    <img src="readme-assets\blog-add.PNG" width="300px"/>
</p>

The edit blogs page uses the same form as the add blogs page but is pre filled will the info from the blog that was selected to edit. Selecting confirm will update that blogs info in the database, the cancel button will return you to the blogs page.

<p align="center">
    <img src="readme-assets\blog-edit.PNG" width="300px"/>
</p>

### Profile

The profile page contains a form detailing a users stored info including a checkbox details the users current subscription to mailing list status. If the user has saved data previously these will be pre filled, if they are already signed up for the mailing list the checkbox will be checked. The profile page also contains controls to manage subscriptions by opening the stripe customer portal and controls to delete suer account. When logged in as an admin there will also be an additional control to navigate to the send newsletter page.

<p align="center">
    <img src="readme-assets\profile.PNG" width="300px"/>
</p>

### Mailing

The subscribe to mailing page contains a form with a single field for the users email. If the user is logged in and already has an email address associated with their profile this field will be pre filled. Filling in the field and selecting register will add that address to the mailing list. If the entered email address is already part of the mailing list the user wil receive a toast message to inform them of this and no action will be taken.

<p align="center">
    <img src="readme-assets\newsletter.PNG" width="300px"/>
</p>

The unsubscribe from mailing list page uses the same form from the subscribe page and is also pre filled if the user is logged in and has a registered email address. Filling in the field and selecting submit will remove that address from the mailing list if it is present. If the entered email address is not present in the mailing list the user wil receive a toast message to inform them of this and no action will be taken.

<p align="center">
    <img src="readme-assets\newsletter-unsubscribe.PNG" width="300px"/>
</p>

When admin users are logged in they can access the send newsletter page from their profile page. This page consists of a form with fields for subject and message. Filling in these fields and selecting 'Send' will send an email with these details to each email address in the mailing list.

<p align="center">
    <img src="readme-assets\send-newsletter.PNG" width="300px"/>
</p>

### Auth

Auth is handled by django-allauth but all pages have been edited and restyled to match the rest of the website.

#### Log In

The sing in page contains a form which the user can use to log in if that have already registered for an account. Simply enter their details and select sign in. selecting the forgot password button will direct the user to the password reset page. If they do not have an account there is a link to direct them to do so.

<p align="center">
    <img src="readme-assets\sign-in.PNG" width="300px"/>
</p>

#### Sign Out

The sign out page asks the user to confirm the wish to sign out. Clicking the sign out button will log the user out and redirect the user to the homepage.

<p align="center">
    <img src="readme-assets\log-out.PNG" width="150px"/>
</p>

#### Register

The register page contains a form the user can use to create an account. They must ender all relevant details before clicking the sign up button and confirming their email address before logging in.

<p align="center">
    <img src="readme-assets\register.PNG" width="300px"/>
</p>

### Error Pages

Custom error pages for 404 and 500 errors contain a simple box showing the error type and a button to return to the site homepage.

<p align="center">
    <img src="readme-assets\error404.PNG" width="300px"/>
</p>

## Testing

For full testing documentation please see [TESTING.md](TESTING.md)

## Deployment

### Deploying to Heroku

To deploy this application to heroku first we must make sure to establish a requirements.txt and Procfile as heroku needs these to operate. First type:

```sh
pip3 freeze --local > requirements.txt
```

into the terminal to establish your requirements.txt file. Then enter:

```sh
echo web: gunicorn tippy.wsgi:application > Procfile
```

to insert the startup commands for heroku into a Procfile.

- Next, go to [Heroku](https://www.heroku.com/) and login/register
- Navigate to your dashboard and select 'New' - 'Create new app'
- Enter a unique application name and select your region then click 'Create app'
- Navigate to the new apps overview page, under installed add-ons click 'configure Add-ons'. Search for 'Heroku Postgres' and select to add it to add-ons.
- To connect your app and set up automatic deployment, select 'GitHub' under the 'Deployment method' section.
- Select your GitHub profile and the name of the repository containing your code.
- Add your config variables to Heroku by navigating to settings, scrolling down and clicking 'Reveal Config Vars'. Then input the key value pairs from your `.env` file
- Return to the deploy tab and select 'Enable Automatic deployment'
- Once the app is deployed you can open the live site by selecting the 'Open app' button at the top right of the page.

### Configuring Stripe

### Configuring Gmail

- Log in to gmail.
- Navigate to settings, then select accounts and Import > other google account settings > Security > Signing into google.
- Click to turn on 2 step verification and follow instructions to verify.
- Return to the security page and select the new option 'App passwords' under signing into google.
- For app select 'Mail' and under select device select other and type 'django'.
- Copy the generated app password and save it as a config variable in heroku along with the gmail email account.
  ```
  EMAIL_HOST_PASS: generatedAppPassword
  EMAIL_HOST_USER: example@gmail.com
  ```

### Configuring AWS S3

- Log in to AWS.
- Search for s3 and select it
- On the buckets page select create bucket, add bucket name and select local region. Under object ownership click ACLs enabled and bucket owner preferred. Uncheck 'Block all public access' and create bucket.
- Navigate to the new buckets properties tab

### Cloning and running locally

- To clone the repository for this project first navigate to the [Repository main page](https://github.com/ChronoLogic12/tippy-tea-subscription) and click on the **code** button.

<p align="center">
    <img src="readme-assets\clone-code.PNG" width="500px"/>
</p>

- To clone the repository using HTTPS, select the HTTPS tab under the clone section and click the icon to copy the provided url to the clipboard.

<p align="center">
    <img src="readme-assets\clone-https.PNG" width="200px"/>
</p>

- Open Git Bash and navigate to the location you would like to store the cloned repository.
- Type `git clone` followed by the url you copied earlier.

```sh
$ git clone https://github.com/ChronoLogic12/bookmarks.git
```

- Press enter to create your cloned repository.
- In bash navigate to the root directory of the downloaded project and run the following command to create a shell and install dependencies.

```sh
pipenv shell
pipenv install
```

- At the project root directory create a file called `.env`.
- in `.env` add the following environment variable data and replace empty strings with your stripe key data.

```py
SECRET_KEY = ''
STRIPE_PUBLIC_KEY = ''
STRIPE_SECRET_KEY = ''
STRIPE_WH_SECRET = ''
DEVELOPMENT = 'True'
```

- To run a local development server from Bash:

```sh
python3 manage.py runserver
```

run on http://localhost:8000/

For more details on cloning repositories click [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

## Credits

### Services

- [Materialize](https://materializecss.com/) - layout, interactive components, element styling, text colours and icons.
- [Google fonts](https://fonts.google.com/).
- [Font Awesome](https://fontawesome.com/) - general additional icons.
- [Django](https://www.djangoproject.com/) python framework.
- [Stripe documentation](https://stripe.com/docs/billing/quickstart) - checkout app was adapted from code found in the stripe docs billing quick start guid.
- [djstripe](https://dj-stripe.dev/) linking between django and stripe.
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
