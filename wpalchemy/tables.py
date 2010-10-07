import sqlalchemy as sa

metadata = sa.MetaData()

comments = sa.Table('wp_comments', metadata,
    sa.Column('comment_ID', sa.Integer(), primary_key=True, nullable=False),
    sa.Column('comment_post_ID', sa.Integer(), primary_key=False, nullable=False),
    sa.Column('comment_author', sa.Text(length=None), primary_key=False, nullable=False),
    sa.Column('comment_author_email', sa.String(length=100), primary_key=False, nullable=False),
    sa.Column('comment_author_url', sa.String(length=200), primary_key=False, nullable=False),
    sa.Column('comment_author_IP', sa.String(length=100), primary_key=False, nullable=False),
    sa.Column('comment_date', sa.DateTime(timezone=False), primary_key=False, nullable=False),
    sa.Column('comment_date_gmt', sa.DateTime(timezone=False), primary_key=False, nullable=False),
    sa.Column('comment_content', sa.Text(length=None), primary_key=False, nullable=False),
    sa.Column('comment_karma', sa.Integer(), primary_key=False, nullable=False),
    sa.Column('comment_approved', sa.String(length=4), primary_key=False, nullable=False),
    sa.Column('comment_agent', sa.String(length=255), primary_key=False, nullable=False),
    sa.Column('comment_type', sa.String(length=20), primary_key=False, nullable=False),
    sa.Column('comment_parent', sa.Integer(), primary_key=False, nullable=False),
    sa.Column('user_id', sa.Integer(), primary_key=False, nullable=False),
    sa.ForeignKeyConstraint(['comment_post_ID'], ['wp_posts.ID']),
    sa.ForeignKeyConstraint(['comment_parent'], ['wp_comments.comment_ID']),
    sa.ForeignKeyConstraint(['user_id'], ['wp_users.ID']),
)

links = sa.Table('wp_links', metadata,
    sa.Column('link_id', sa.Integer(), primary_key=True, nullable=False),
    sa.Column('link_url', sa.String(length=255), primary_key=False, nullable=False),
    sa.Column('link_name', sa.String(length=255), primary_key=False, nullable=False),
    sa.Column('link_image', sa.String(length=255), primary_key=False, nullable=False),
    sa.Column('link_target', sa.String(length=25), primary_key=False, nullable=False),
    sa.Column('link_category', sa.Integer(), primary_key=False, nullable=False),
    sa.Column('link_description', sa.String(length=255), primary_key=False, nullable=False),
    sa.Column('link_visible', sa.String(length=1), primary_key=False, nullable=False),
    sa.Column('link_owner', sa.Integer(), primary_key=False, nullable=False),
    sa.Column('link_rating', sa.Integer(), primary_key=False, nullable=False),
    sa.Column('link_updated', sa.DateTime(timezone=False), primary_key=False, nullable=False),
    sa.Column('link_rel', sa.String(length=255), primary_key=False, nullable=False),
    sa.Column('link_notes', sa.Text(length=None), primary_key=False, nullable=False),
    sa.Column('link_rss', sa.String(length=255), primary_key=False, nullable=False),
    sa.ForeignKeyConstraint(['link_owner'], ['wp_users.ID']),
)

options = sa.Table('wp_options', metadata,
    sa.Column('option_id', sa.Integer(), primary_key=True, nullable=False),
    sa.Column('blog_id', sa.Integer(), primary_key=True, nullable=False),
    sa.Column('option_name', sa.String(length=64), primary_key=True, nullable=False),
    sa.Column('option_value', sa.Text(length=None), primary_key=False, nullable=False),
    sa.Column('autoload', sa.String(length=3), primary_key=False, nullable=False),
)

postmeta = sa.Table('wp_postmeta', metadata,
    sa.Column('meta_id', sa.Integer(), primary_key=True, nullable=False),
    sa.Column('post_id', sa.Integer(), primary_key=False, nullable=False),
    sa.Column('meta_key', sa.String(length=255), primary_key=False),
    sa.Column('meta_value', sa.Text(length=None), primary_key=False),
    sa.ForeignKeyConstraint(['post_id'], ['wp_posts.ID']),
)

posts = sa.Table('wp_posts', metadata,
    sa.Column('ID', sa.Integer(), primary_key=True, nullable=False),
    sa.Column('post_author', sa.Integer(), primary_key=False, nullable=False),
    sa.Column('post_date', sa.DateTime(timezone=False), primary_key=False, nullable=False),
    sa.Column('post_date_gmt', sa.DateTime(timezone=False), primary_key=False, nullable=False),
    sa.Column('post_content', sa.Text(length=None), primary_key=False, nullable=False),
    sa.Column('post_title', sa.Text(length=None), primary_key=False, nullable=False),
    sa.Column('post_category', sa.Integer(), primary_key=False, nullable=False),
    sa.Column('post_excerpt', sa.Text(length=None), primary_key=False, nullable=False),
    sa.Column('post_status', sa.String(length=10), primary_key=False, nullable=False),
    sa.Column('comment_status', sa.String(length=15), primary_key=False, nullable=False),
    sa.Column('ping_status', sa.String(length=6), primary_key=False, nullable=False),
    sa.Column('post_password', sa.String(length=20), primary_key=False, nullable=False),
    sa.Column('post_name', sa.String(length=200), primary_key=False, nullable=False),
    sa.Column('to_ping', sa.Text(length=None), primary_key=False, nullable=False),
    sa.Column('pinged', sa.Text(length=None), primary_key=False, nullable=False),
    sa.Column('post_modified', sa.DateTime(timezone=False), primary_key=False, nullable=False),
    sa.Column('post_modified_gmt', sa.DateTime(timezone=False), primary_key=False, nullable=False),
    sa.Column('post_content_filtered', sa.Text(length=None), primary_key=False, nullable=False),
    sa.Column('post_parent', sa.Integer(), primary_key=False, nullable=False),
    sa.Column('guid', sa.String(length=255), primary_key=False, nullable=False),
    sa.Column('menu_order', sa.Integer(), primary_key=False, nullable=False),
    sa.Column('post_type', sa.String(length=20), primary_key=False, nullable=False),
    sa.Column('post_mime_type', sa.String(length=100), primary_key=False, nullable=False),
    sa.Column('comment_count', sa.Integer(), primary_key=False, nullable=False),
    sa.ForeignKeyConstraint(['post_author'], ['wp_users.ID']),
    sa.ForeignKeyConstraint(['post_parent'], ['wp_posts.ID']),
)

term_relationships = sa.Table('wp_term_relationships', metadata,
    sa.Column('object_id', sa.Integer(), primary_key=True, nullable=False),
    sa.Column('term_taxonomy_id', sa.Integer(), primary_key=True, nullable=False),
    sa.ForeignKeyConstraint(['term_taxonomy_id'], ['wp_term_taxonomy.term_taxonomy_id']),
)

term_taxonomy = sa.Table('wp_term_taxonomy', metadata,
    sa.Column('term_taxonomy_id', sa.Integer(), primary_key=True, nullable=False),
    sa.Column('term_id', sa.Integer(), primary_key=False, nullable=False),
    sa.Column('taxonomy', sa.String(length=32), primary_key=False, nullable=False),
    sa.Column('description', sa.Text(length=None), primary_key=False, nullable=False),
    sa.Column('parent', sa.Integer(), primary_key=False, nullable=False),
    sa.Column('count', sa.Integer(), primary_key=False, nullable=False),
    sa.UniqueConstraint('term_id', 'taxonomy'),
    sa.ForeignKeyConstraint(['term_id'], ['wp_terms.term_id']),
    sa.ForeignKeyConstraint(['parent'], ['wp_term_taxonomy.term_taxonomy_id']),
)

terms = sa.Table('wp_terms', metadata,
    sa.Column('term_id', sa.Integer(), primary_key=True, nullable=False),
    sa.Column('name', sa.String(length=55), primary_key=False, nullable=False),
    sa.Column('slug', sa.String(length=200), primary_key=False, nullable=False),
    sa.Column('term_group', sa.Integer(), primary_key=False, nullable=False),
    sa.UniqueConstraint('slug'),
)

usermeta = sa.Table('wp_usermeta', metadata,
    sa.Column('umeta_id', sa.Integer(), primary_key=True, nullable=False),
    sa.Column('user_id', sa.Integer(), primary_key=False, nullable=False),
    sa.Column('meta_key', sa.String(length=255), primary_key=False),
    sa.Column('meta_value', sa.Text(length=None), primary_key=False),
    sa.ForeignKeyConstraint(['user_id'], ['wp_users.ID']),
)

users = sa.Table('wp_users', metadata,
    sa.Column('ID', sa.Integer(), primary_key=True, nullable=False),
    sa.Column('user_login', sa.String(length=60), primary_key=False, nullable=False),
    sa.Column('user_pass', sa.String(length=64), primary_key=False, nullable=False),
    sa.Column('user_nicename', sa.String(length=50), primary_key=False, nullable=False),
    sa.Column('user_email', sa.String(length=100), primary_key=False, nullable=False),
    sa.Column('user_url', sa.String(length=100), primary_key=False, nullable=False),
    sa.Column('user_registered', sa.DateTime(timezone=False), primary_key=False, nullable=False),
    sa.Column('user_activation_key', sa.String(length=60), primary_key=False, nullable=False),
    sa.Column('user_status', sa.Integer(), primary_key=False, nullable=False),
    sa.Column('display_name', sa.String(length=250), primary_key=False, nullable=False),
)