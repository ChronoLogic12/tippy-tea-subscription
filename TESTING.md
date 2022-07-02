# **Tippy** - Testing

<p align="center">
    <img src="readme-assets/tippy-logo-round.png" width="200px"/>
</p>

[README.md](README.md)

## **Table of contents**

- [**Tippy** - Testing](#tippy---testing)
  - [**Table of contents**](#table-of-contents)
  - [**Bugs**](#bugs)

## **Bugs**

- When using a materialize dropdown component to display a delete confirmation button for each blog post created on the all blogs page I noticed that the delete confirmation buttons for each post were all being created with the ID for the first blog post rendered. This meant that selecting any delete confirmation button would delete the first post rendered to the page rather than its related post. The reason for this was that the 'data-target' attribute and the matching dropdown 'id' were the same for each card meaning there was only ever one instance of the dropdown component created. To correct for this I appended the blog posts unique id value to the 'data-target' and 'id' attributes for the dropdown elements on each card so that a unique dropdown would be created for each blog post.

```html
<a class="right red-text dropdown-trigger" href="#" data-target="delete-confirmation{{blog.id}}">
	delete
</a>
<ul id="delete-confirmation{{blog.id}}" class="dropdown-content">
	<li><a class="red-text" href="{% url 'delete_blog' blog.id %}">Confirm</a></li>
	<li><a class="grey-text" href="#!">Cancel</a></li>
</ul>
```
