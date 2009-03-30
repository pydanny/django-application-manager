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

package_identifier_doc ="""
This is the application module name.
<blockquote>
    <strong>Blog:</strong> blog<br />
    <strong>Bookmarks:</strong> bookmarks
</blockquote>
"""

model_identifier_doc = """
This is the application model name.
<blockquote>
    <strong>Blog:</strong> Post<br />
    <strong>Bookmarks:</strong> BookmarkInstance<br />
</blockquote>
"""

sample_limit_doc = """
This shows how many samples of a particular type to display.<br />
A good number is 0-3 items and we might replace the text field with a
numerical select widget.
"""

item_url_doc = """
This describes the attribute or method where the link to a sample is fetched from.<br />
In most cases you can just use get_absolute_url. 
<blockquote>
    <strong>Blog:</strong> get_absolute_url<br />
    <strong>Bookmarks:</strong> bookmark.url<br />
</blockquote>
"""

item_title_doc = """
This describes where the title for samples is stored.
<blockquote>
    <strong>Blog:</strong> title<br />
    <strong>Bookmarks:</strong> description<br />
</blockquote>
"""

item_description_doc = """
This describes where the description or tease is displayed.
<blockquote>
    <strong>Blog:</strong> tease<br />
    <strong>Bookmarks:</strong> note<br />
</blockquote>
"""

url_name_doc = """
Enter url names as set in urls.py:
<blockquote>
    <strong>Blog:</strong> blog_new<br />
    <strong>Bookmarks:</strong> add_bookmark<br />
</blockquote>

"""

applink_title_doc ="""
Enter a human readable title:
<blockquote>
    <strong>Blog:</strong> Add blog entry<br />
    <strong>Bookmarks:</strong> Add Bookmark<br />
</blockquote>
"""

applink_description_doc = """
<blockquote>
    <strong>Blog:</strong> Submit a blog entry.<br />
    <strong>Bookmarks:</strong> Add a bookmark to this site.<br />
</blockquote>
"""

base = """
<blockquote>
    <strong>Blog:</strong> xyz<br />
    <strong>Bookmarks:</strong> xyz<br />
</blockquote>

"""