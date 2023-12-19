from datetime import datetime

class Post:
    def __init__(self, title, content, author, timestamp=None):
        self.title = title
        self.content = content
        self.author = author
        self.timestamp = timestamp or datetime.now()

    def __str__(self):
        return f"{self.title} by {self.author} on {self.timestamp}"

class Author:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Blog:
    def __init__(self, name):
        self.name = name
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)
        print(f"New post added to {self.name}: {post}")

    def display_posts_by_author(self, author):
        author_posts = [post for post in self.posts if post.author == author]
        if not author_posts:
            print(f"No posts found by {author}.")
        else:
            print(f"Posts by {author} in {self.name}:")
            for post in author_posts:
                print(post)

    def display_latest_posts(self, num_posts=5):
        if not self.posts:
            print("No posts available.")
        else:
            sorted_posts = sorted(self.posts, key=lambda post: post.timestamp, reverse=True)
            print(f"Latest {min(num_posts, len(sorted_posts))} posts in {self.name}:")
            for post in sorted_posts[:num_posts]:
                print(post)

# Example usage:

# Create authors
author1 = Author("Alice")
author2 = Author("Bob")

# Create a blog
tech_blog = Blog("Tech Blog")

# Create posts
post1 = Post("Introduction to Python", "Python is a versatile programming language.", author1)
post2 = Post("Web Development Trends", "Explore the latest trends in web development.", author2)
post3 = Post("Machine Learning Basics", "An overview of machine learning concepts.", author1)

# Add posts to the blog
tech_blog.add_post(post1)
tech_blog.add_post(post2)
tech_blog.add_post(post3)

# Display posts by a specific author
tech_blog.display_posts_by_author(author1)

# Display the latest posts
tech_blog.display_latest_posts()
