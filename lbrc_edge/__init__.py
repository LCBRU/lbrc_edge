from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class EdgeSiteStudy(db.Model):
    __tablename__ = 'edge_site_study'
    __bind_key__ = 'etl_central'

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer)
    mrec_number = db.Column(db.String)
    iras_number = db.Column(db.String)
    project_full_title = db.Column(db.String)
    project_short_title = db.Column(db.String)
    project_phase = db.Column(db.String)
    primary_clinical_management_areas = db.Column(db.String)
    project_site_status = db.Column(db.String)
    project_status = db.Column(db.String)
    project_site_rand_submission_date = db.Column(db.Date)
    project_site_start_date_nhs_permission = db.Column(db.Date)
    project_site_date_site_confirmed = db.Column(db.Date)
    project_site_planned_closing_date = db.Column(db.Date)
    project_site_closed_date = db.Column(db.Date)
    project_site_planned_recruitment_end_date = db.Column(db.Date)
    project_site_actual_recruitment_end_date = db.Column(db.Date)
    principal_investigator = db.Column(db.String)
    project_site_target_participants = db.Column(db.Integer)
    project_site_estimated_annual_target = db.Column(db.Integer)
    recruited_org = db.Column(db.Integer)
    project_site_lead_nurses = db.Column(db.String)
    project_site_name = db.Column(db.String)
    project_type = db.Column(db.String)
    nihr_portfolio_study_id = db.Column(db.Integer)
    pi_orcidid = db.Column(db.String)
    is_uhl_lead_centre = db.Column(db.Boolean)
    lead_centre_name_if_not_uhl = db.Column(db.String)
    cro_cra_used = db.Column(db.Boolean)
    name_of_cro_cra_company_used = db.Column(db.String)
    study_category = db.Column(db.String)
    randomised_name = db.Column(db.String)
    name_of_brc_involved = db.Column(db.String)
