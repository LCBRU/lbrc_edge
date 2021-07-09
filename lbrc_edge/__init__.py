from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

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

    @property
    def effective_recruitment_start_date(self):
        return self.project_site_start_date_nhs_permission or self.project_site_date_site_confirmed

    @property
    def effective_recruitment_end_date(self):
        return self.project_site_actual_recruitment_end_date or self.project_site_planned_recruitment_end_date

    def target_requirement_by(self, end_date):
        if self.effective_recruitment_start_date is None or self.project_site_target_participants is None or self.effective_recruitment_end_date is None:
            return None
        
        return self.project_site_target_participants * (self.effective_recruitment_start_date - end_date) / (self.effective_recruitment_start_date - self.effective_recruitment_end_date)

    @property
    def current_target_recruited_percent(self):
        target_by_now = self.target_requirement_by(datetime.now.date())

        if target_by_now is None:
            return None

        recruited = self.recruited_org or 0
        
        return recruited * 100 / target_by_now

    @property
    def rag_rating(self):
        target_perc_now = self.current_target_recruited_percent

        if target_perc_now is None:
            return None

        if target_perc_now >= 100:
            return 'green'
        elif target_perc_now < 80:
            return 'red'
        else:
            return 'amber'
