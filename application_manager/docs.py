app_title_doc = """
This is how the application is titled for the user and will appear in links.<br />
Our examples will be <strong>Bookmarks</strong> and <strong>Blog</strong>.
"""
app_description_doc = """
This should be a very short description of your application. Examples:
<blockquote>
    <strong>Blog:</strong> A blog is usually maintained by an individual with regular entries of commentary and descriptions of events.<br />
    <strong>Bookmarks:</strong> Internet bookmarks are stored Web page locations (URLs) that can be retrieved.<br />
</blockquote>
"""

master_url_name_doc = """
Enter the link used in Navigation display:
<blockquote>
    <strong>Blog:</strong> blog_list_yours<br />
    <strong>Bookmarks:</strong> your_bookmarks
</blockquote>
"""


active_doc = """
Is this application turned on across the site?<br />
If it is not active, then no one will be able to see links.
"""

user_lookup_name_doc ="""
This is the user lookup name for determination of samples displayed.<br />
This is taken from the ForeignKey field from the object to the User object.
<blockquote>
    <strong>Blog:</strong> author<br />
    <strong>Bookmarks:</strong> user
</blockquote>
"""

base = """
<blockquote>
    <strong>Blog:</strong> 
    <strong>Bookmarks:</strong> 
</blockquote>

"""