package com.SAR_Generator.main_service.dto;

import java.time.LocalDate;

import lombok.Data;

@Data
public class CustomerKycRequest {

    private String customer_id;
    private String full_name;
    private LocalDate dob;
    private String pan;
    private String aadhaar_last4;
    private String occupation;
    private Long declared_annual_income;
    private String risk_category;
    private String address;
    private LocalDate kyc_last_updated;
}