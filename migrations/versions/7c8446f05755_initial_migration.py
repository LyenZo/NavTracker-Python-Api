"""Initial migration.

Revision ID: 7c8446f05755
Revises: 
Create Date: 2025-04-09 05:19:17.388846

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c8446f05755'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('punto',
    sa.Column('id_punto', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=20), nullable=False),
    sa.Column('latitud', sa.Numeric(precision=18, scale=15), nullable=False),
    sa.Column('longitud', sa.Numeric(precision=18, scale=15), nullable=False),
    sa.Column('direccion', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id_punto')
    )
    op.create_table('rastreo',
    sa.Column('id_rastreo', sa.Integer(), nullable=False),
    sa.Column('lat', sa.Float(precision=6), nullable=False),
    sa.Column('lng', sa.Float(precision=6), nullable=False),
    sa.Column('altitud', sa.Numeric(precision=10, scale=3), nullable=False),
    sa.Column('velocidad', sa.Numeric(precision=5, scale=3), nullable=False),
    sa.Column('hora', sa.Time(), nullable=False),
    sa.Column('fecha', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id_rastreo')
    )
    op.create_table('ruta',
    sa.Column('id_ruta', sa.Integer(), nullable=False),
    sa.Column('id_conductor', sa.Integer(), nullable=False),
    sa.Column('id_pasajero', sa.Integer(), nullable=False),
    sa.Column('lat_inicio', sa.Numeric(precision=9, scale=6), nullable=False),
    sa.Column('lon_inicio', sa.Numeric(precision=9, scale=6), nullable=False),
    sa.Column('lat_final', sa.Numeric(precision=9, scale=6), nullable=False),
    sa.Column('lon_final', sa.Numeric(precision=9, scale=6), nullable=False),
    sa.Column('f_inicio', sa.DateTime(), nullable=False),
    sa.Column('f_final', sa.DateTime(), nullable=False),
    sa.Column('distancia', sa.Numeric(precision=9, scale=6), nullable=False),
    sa.PrimaryKeyConstraint('id_ruta')
    )
    op.create_table('tipo',
    sa.Column('id_tipo', sa.Integer(), nullable=False),
    sa.Column('tipo', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id_tipo')
    )
    op.create_table('usuario',
    sa.Column('id_u', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=20), nullable=False),
    sa.Column('ap_pat', sa.String(length=20), nullable=False),
    sa.Column('ap_mat', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('n_tel', sa.String(length=20), nullable=True),
    sa.Column('id_tipo', sa.Integer(), nullable=False),
    sa.Column('id_vehiculo', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id_u'),
    sa.UniqueConstraint('email')
    )
    op.create_table('vehiculo',
    sa.Column('id_vehiculo', sa.Integer(), nullable=False),
    sa.Column('vehiculo', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id_vehiculo')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vehiculo')
    op.drop_table('usuario')
    op.drop_table('tipo')
    op.drop_table('ruta')
    op.drop_table('rastreo')
    op.drop_table('punto')
    # ### end Alembic commands ###
