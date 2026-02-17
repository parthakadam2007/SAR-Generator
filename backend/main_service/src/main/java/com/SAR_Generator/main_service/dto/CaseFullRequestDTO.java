package com.SAR_Generator.main_service.dto;


import lombok.*;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.time.OffsetDateTime;
import java.util.List;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class CaseFullRequestDTO {

    private String case_id;

    private OffsetDateTime generated_at;

    private String institution;

    private CustomerKycRequest customer_kyc;

    private AccountProfileRequest account_profile;

    private List<AlertRequest> alerts;

    private List<TransactionRequest> transactions;
}