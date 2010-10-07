import sqlalchemy as sa
import sqlalchemy.orm as orm
import tables

metadata = tables.metadata

class Term(object):
    def __init__(self, name, slug, term_group=0):
        self.name = name
        self.slug = slug
        self.term_group = term_group

    def __repr__(self):
        return '<Term(%r, %r, %r)>' % (self.name, self.slug, self.term_group)

class Taxonomy(object):
    def __init__(self, term, description):
        self.term = term
        self.description = description

class PostTag(Taxonomy):
    def __repr__(self):
        return '<PostTag(%r, %r)>' % (self.term, self.description)

class Category(Taxonomy):
    def __repr__(self):
        return '<Category(%r, %r)>' % (self.term, self.description)

class LinkCategory(Taxonomy):
    def __repr__(self):
        return '<LinkCategory(%r, %r)>' % (self.term, self.description)

class Post(object):
    def __init__(self, post_title, post_type='post'):
        self.post_title = post_title
        self.post_type = post_type

    def __repr__(self):
        return '<Post(%r, %r)>' % (self.post_title, self.post_type)

class PostMeta(object):
    def __init__(self, meta_key, meta_value):
        self.meta_key = meta_key
        self.meta_value = meta_value

    def __repr__(self):
        return '<PostMeta(%r, %r)>' % (self.meta_key, self.meta_value)

class Link(object):
    def __init__(self, link_url, link_name):
        self.link_url = link_url
        self.link_name = link_name

    def __repr__(self):
        return '<Link(%r, %r)>' % (self.link_url, self.link_name)

class Comment(object):
    def __init__(self, comment_author, comment_content):
        self.comment_author = comment_author
        self.comment_content = comment_content

    def __repr__(self):
        return '<Comment(%r, %r)>' % (self.comment_author, self.comment_content)

class User(object):
    def __init__(self, user_login):
        self.user_login = user_login

    def __repr__(self):
        return '<User(%r)>' % self.user_login

class UserMeta(object):
    def __init__(self, meta_key, meta_value):
        self.meta_key = meta_key
        self.meta_value = meta_value

    def __repr__(self):
        return '<UserMeta(%r, %r)>' % (self.meta_key, self.meta_value)

class Option(object):
    def __init__(self, option_name, option_value):
        self.option_name = option_name
        self.option_value = option_value

    def __repr__(self):
        return '<Option(%r, %r)>' % (self.option_name, self.option_value)

orm.mapper(Term, tables.terms)

taxonomy_mapper = orm.mapper(
    Taxonomy,
    tables.term_taxonomy,
    properties={'term': orm.relation(Term)},
    polymorphic_on=tables.term_taxonomy.c.taxonomy,
)

orm.mapper(
    PostTag,
    properties={
        'posts': orm.dynamic_loader(
            Post,
            secondary=tables.term_relationships,
            primaryjoin=(tables.term_taxonomy.c.term_taxonomy_id
                         == tables.term_relationships.c.term_taxonomy_id),
            secondaryjoin=(tables.term_relationships.c.object_id
                           == tables.posts.c.ID),
            foreign_keys=[tables.term_relationships.c.object_id,
                          tables.term_relationships.c.term_taxonomy_id],
        ),
    },
    inherits=taxonomy_mapper,
    polymorphic_identity='post_tag',
)

orm.mapper(
    Category,
    properties={
        'children': orm.relation(
            Category,
            backref=orm.backref('parent_category',
                                remote_side=[tables.term_taxonomy.c.term_taxonomy_id]),
        ),
        'posts': orm.dynamic_loader(
            Post,
            secondary=tables.term_relationships,
            primaryjoin=(tables.term_taxonomy.c.term_taxonomy_id
                         == tables.term_relationships.c.term_taxonomy_id),
            secondaryjoin=(tables.term_relationships.c.object_id
                           == tables.posts.c.ID),
            foreign_keys=[tables.term_relationships.c.object_id,
                          tables.term_relationships.c.term_taxonomy_id],
        ),
    },
    inherits=taxonomy_mapper,
    polymorphic_identity='category',
)

orm.mapper(
    LinkCategory,
    properties={
        'links': orm.relation(
            Link,
            secondary=tables.term_relationships,
            primaryjoin=(tables.term_taxonomy.c.term_taxonomy_id
                         == tables.term_relationships.c.term_taxonomy_id),
            secondaryjoin=(tables.term_relationships.c.object_id
                           == tables.links.c.link_id),
            foreign_keys=[tables.term_relationships.c.object_id,
                          tables.term_relationships.c.term_taxonomy_id],
        ),
    },
    inherits=taxonomy_mapper,
    polymorphic_identity='link_category',
)

orm.mapper(
    Post,
    tables.posts,
    properties={
        'meta': orm.relation(
            PostMeta,
            collection_class=orm.collections.column_mapped_collection(tables.postmeta.c.meta_key),
        ),
        'children': orm.relation(
            Post,
            backref=orm.backref('parent', remote_side=[tables.posts.c.ID]),
        ),
        'tags': orm.relation(
            PostTag,
            secondary=tables.term_relationships,
            primaryjoin=(tables.posts.c.ID
                         == tables.term_relationships.c.object_id),
            secondaryjoin=(tables.term_relationships.c.term_taxonomy_id
                           == tables.term_taxonomy.c.term_taxonomy_id),
            foreign_keys=[tables.term_relationships.c.object_id,
                          tables.term_relationships.c.term_taxonomy_id],
        ),
        'categories': orm.relation(
            Category,
            secondary=tables.term_relationships,
            primaryjoin=(tables.posts.c.ID
                         == tables.term_relationships.c.object_id),
            secondaryjoin=(tables.term_relationships.c.term_taxonomy_id
                           == tables.term_taxonomy.c.term_taxonomy_id),
            foreign_keys=[tables.term_relationships.c.object_id,
                          tables.term_relationships.c.term_taxonomy_id],
        ),
        'comments': orm.relation(Comment, backref='post'),
    },
)

orm.mapper(PostMeta, tables.postmeta)

orm.mapper(
    Link,
    tables.links,
    properties={
        'categories': orm.relation(
            LinkCategory,
            secondary=tables.term_relationships,
            primaryjoin=(tables.links.c.link_id
                         == tables.term_relationships.c.object_id),
            secondaryjoin=(tables.term_relationships.c.term_taxonomy_id
                           == tables.term_taxonomy.c.term_taxonomy_id),
            foreign_keys=[tables.term_relationships.c.object_id,
                          tables.term_relationships.c.term_taxonomy_id],
        ),
    },
)

orm.mapper(
    Comment,
    tables.comments,
    properties={
        'children': orm.relation(
            Comment,
            backref=orm.backref('parent',
                                remote_side=[tables.comments.c.comment_ID]),
        ),
    },
)

orm.mapper(
    User,
    tables.users,
    properties={
        'meta': orm.relation(
            UserMeta,
            collection_class=orm.collections.column_mapped_collection(tables.usermeta.c.meta_key),
        ),
        'posts': orm.dynamic_loader(Post, backref='user'),
        'links': orm.dynamic_loader(Link, backref='user'),
        'comments': orm.dynamic_loader(Comment, backref='user'),
    },
)

orm.mapper(UserMeta, tables.usermeta)

orm.mapper(Option, tables.options)
