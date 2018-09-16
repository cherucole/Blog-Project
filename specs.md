![Cherucole's-Blog](https://www.lifesafar.com/wp-content/uploads/2018/01/blog.jpg)

A way for users to submit one minute pitches depending on the category they like.
The app is live here [Pitchify-pro](https://cherucole-blog.herokuapp.com/).


Features
========

- Built with Python 3 (3.7+) and Flask
- Shows 'blogs','categories' and sorted by post date
- Styled using Bootstrap
- Handles external get posts and requests from database
- Get news articles from several sources (`choose from landing page`)


Installation
========

    $ git clone <repository_url>


Usage
========

**NOTE:** You need to have fully cloned it to run it locally.


    $ ./start.sh 

    # it will launch the web page from local server and fetch 
    articles from database


API Object Reference
========

## Classes: `user, Pitch`


**Arguments:**

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| `Post` | string | No | pitches from this category only and sorted by relevancy. | `(empty string)`  |
| `user` | integer | No | Returns the user from this database source only. | `(user's choice)` |



## Class: `posts`

Each `post` has the following properties

- **title** - post name
- **id** - post unique id
- **content** - the post content
- **post date** - Date aricle was created

## Class: `User`

Each `User` has the following properties

- **id** - unique id of the user in system
- **username** - name stored on database
- **email** - user email
- **image url** - profile picture for user

Tests
========

To run the tests locally just do:

    $ cd app
    $ python3.7 test_users.py


The tests are run on a local test server.

Contribute
========

If you want to add any new features, or improve existing ones, feel free to send a pull request!