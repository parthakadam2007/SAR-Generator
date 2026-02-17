package com.SAR_Generator.main_service.dto;

import java.time.LocalDate;

import lombok.Data;

@Data
public class AccountProfileRequest {

    private String account_number;
    private String account_type;
    private LocalDate opened_date;
    private Long average_monthly_balance;
    private Long average_monthly_credit;
    private Long average_monthly_debit;
    private String usual_transaction_pattern;
}