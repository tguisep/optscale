""""Initial"

Revision ID: d5ad8aa61f68
Revises:
Create Date: 2020-06-18 02:39:51.541723

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "d5ad8aa61f68"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "recipient",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("created_at", sa.Integer(), nullable=False),
        sa.Column("role_purpose", sa.String(length=64), nullable=False),
        sa.Column("scope_id", sa.String(length=36), nullable=False),
        sa.Column("user_id", sa.String(length=36), nullable=True),
        sa.Column("meta", sa.TEXT(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint(
            "role_purpose", "scope_id",
            name="uc_recipient_role_purpose_scope_user"
        ),
    )
    op.create_table(
        "report",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("created_at", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=50), nullable=False),
        sa.Column("module_name", sa.String(length=128), nullable=False),
        sa.Column(
            "report_format", sa.Enum("html", name="reportformat"),
            nullable=False
        ),
        sa.Column("template", sa.String(length=128), nullable=False),
        sa.Column("description", sa.TEXT(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name", "module_name",
                            name="uc_report_name_module_name"),
    )
    op.create_table(
        "schedule",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("created_at", sa.Integer(), nullable=False),
        sa.Column("report_id", sa.String(length=36), nullable=False),
        sa.Column("recipient_id", sa.String(length=36), nullable=False),
        sa.Column("crontab", sa.String(length=128), nullable=False),
        sa.Column("last_run", sa.Integer(), nullable=False),
        sa.Column("next_run", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["recipient_id"], ["recipient.id"],
                                ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["report_id"], ["report.id"],
                                ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint(
            "report_id",
            "recipient_id",
            "crontab",
            name="uc_schedule_report_recipient_crontab",
        ),
    )
    op.create_table(
        "task",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("created_at", sa.Integer(), nullable=False),
        sa.Column("schedule_id", sa.String(length=36), nullable=False),
        sa.Column("completed_at", sa.Integer(), nullable=True),
        sa.Column(
            "state",
            sa.Enum(
                "created",
                "started",
                "got_recipients",
                "generating_data",
                "completed",
                "error",
                name="taskstate",
            ),
            nullable=False,
        ),
        sa.Column("result", sa.TEXT(), nullable=True),
        sa.ForeignKeyConstraint(
            ["schedule_id"],
            ["schedule.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("task")
    op.drop_table("schedule")
    op.drop_table("report")
    op.drop_table("recipient")
    # ### end Alembic commands ###
