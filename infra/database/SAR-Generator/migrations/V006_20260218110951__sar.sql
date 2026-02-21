CREATE TABLE sar_reports (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    case_id UUID UNIQUE,
    analysis_id UUID REFERENCES case_analysis(id) ON DELETE CASCADE,

    sar_number VARCHAR(100)  NOT NULL, -- put case_id for now

    sar_summary TEXT NOT NULL, 
    narrative TEXT NOT NULL,
    transaction_analysis TEXT,
    recommended_action TEXT,

    report_status VARCHAR(30) DEFAULT 'Draft',

    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE sar_subjects (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    sar_id UUID REFERENCES sar_reports(id) ON DELETE CASCADE,

    customer_id VARCHAR(50) NOT NULL,
    full_name VARCHAR(150) NOT NULL,
    dob DATE,
    pan VARCHAR(20),
    aadhaar_last4 VARCHAR(4),

    occupation VARCHAR(100),
    declared_annual_income NUMERIC(15,2),
    risk_category VARCHAR(20),

    address TEXT,
    kyc_last_updated DATE
);


CREATE TABLE sar_accounts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    sar_id UUID REFERENCES sar_reports(id) ON DELETE CASCADE,

    account_number VARCHAR(50),
    account_type VARCHAR(50),

    opened_date DATE,

    average_monthly_balance NUMERIC(15,2),
    average_monthly_credit NUMERIC(15,2),
    average_monthly_debit NUMERIC(15,2),

    usual_transaction_pattern TEXT
);


CREATE TABLE sar_risk_assessments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    sar_id UUID REFERENCES sar_reports(id) ON DELETE CASCADE,

    risk_category VARCHAR(20),
    alerts_triggered TEXT,
    inconsistencies TEXT
);


CREATE TABLE sar_indicators (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    sar_id UUID REFERENCES sar_reports(id) ON DELETE CASCADE,

    indicator_text TEXT NOT NULL
);