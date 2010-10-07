# wpalchemy - SQLAlchemy bindings for WordPress

This is a set of SQLAlchemy bindings to the WordPress schema. There is both a
table-level interface and a class-level (ORM) interface.

## Initialization

To use the ORM interface, import `wpalchemy.classes` and use these classes
with a SQLALchemy ORM session:

    import sqlalchemy as sa
    import wpalchemy.classes as wp
    engine = sa.create_engine('mysql://user:password@localhost/blog_db?charset=utf8')
    session = sa.orm.sessionmaker(engine)()

The available classes are: Category, Comment, Link, LinkCategory, Option,
Post, PostMeta, PostTag, Taxonomy, Term, User, and UserMeta.

If you prefer a table-level interface, import `wpalchemy.tables` instead. The
available tables are: comments, links, options, postmeta, posts,
term_relationships, term_taxonomy, terms, usermeta, and users.

## Examples

Here is a simple query and loop that prints the IDs and titles of all pages.

    pages = session.query(wp.Post).filter((wp.Post.post_status == 'publish')
                                          & (wp.Post.post_type == 'page'))
    for page in pages:
        print page.ID, page.post_title

Here's a slightly more complex query that prints the IDs and titles of all
posts published in the past week.

    from datetime import datetime, timedelta
    start_date = datetime.now() - timedelta(7)
    posts = session.query(wp.Post).filter((wp.Post.post_status == 'publish')
                                          & (wp.Post.post_type == 'post')
                                          & (wp.Post.post_date >= start_date))
    for post in posts:
        print post.ID, post.post_title

That's all the documentation I have for now. Please see the source code for
more details.
