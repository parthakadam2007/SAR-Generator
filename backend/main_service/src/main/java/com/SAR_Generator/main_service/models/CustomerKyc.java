package com.SAR_Generator.main_service.models;

import jakarta.persistence.*;
import lombok.*;

import java.time.LocalDate;
import java.util.UUID;

@Entity
@Table(name = "customer_kyc")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class CustomerKyc {

    @Id
    @GeneratedValue
    @Column(columnDefinition = "UUID")
    private UUID id;

    // Many KYC records can belong to one Case (usually 1:1, but safe to use ManyToOne)
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "case_id", nullable = false)
    private Case caseEntity;

    @Column(name = "customer_id", nullable = false, length = 100)
    private String customerId;

    @Column(name = "full_name", length = 255)
    private String fullName;

    private LocalDate dob;

    @Column(length = 20)
    private String pan;

    @Column(name = "aadhaar_last4", length = 4)
    private String aadhaarLast4;

    @Column(length = 255)
    private String occupation;

    @Column(name = "declared_annual_income")
    private Long declaredAnnualIncome;

    @Column(name = "risk_category", length = 50)
    private String riskCategory;

    @Column(columnDefinition = "TEXT")
    private String address;

    @Column(name = "kyc_last_updated")
    private LocalDate kycLastUpdated;
}