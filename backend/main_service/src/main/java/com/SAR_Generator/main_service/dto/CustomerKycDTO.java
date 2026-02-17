package com.SAR_Generator.main_service.dto;

import lombok.*;

import java.time.LocalDate;
import java.util.UUID;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class CustomerKycDTO {

    private UUID id;

    private UUID caseId;

    private String customerId;

    private String fullName;

    private LocalDate dob;

    // Masked fields (important for security)
    private String panMasked;        // XXXX1234
    private String aadhaarMasked;    // ****5678

    private String occupation;

    private Long declaredAnnualIncome;

    private String riskCategory;

    private String address;

    private LocalDate kycLastUpdated;
}