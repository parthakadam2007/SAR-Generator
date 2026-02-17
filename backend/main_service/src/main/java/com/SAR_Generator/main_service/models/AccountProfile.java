package com.SAR_Generator.main_service.models;


import jakarta.persistence.*;
import lombok.*;

import java.time.LocalDate;
import java.util.UUID;

@Entity
@Table(name = "account_profiles")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class AccountProfile {

    @Id
    @GeneratedValue
    @Column(columnDefinition = "UUID")
    private UUID id;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "case_id", nullable = false)
    private Case caseEntity;

    @Column(name = "account_number", length = 50)
    private String accountNumber;

    @Column(name = "account_type", length = 50)
    private String accountType;

    @Column(name = "opened_date")
    private LocalDate openedDate;

    @Column(name = "average_monthly_balance")
    private Long averageMonthlyBalance;

    @Column(name = "average_monthly_credit")
    private Long averageMonthlyCredit;

    @Column(name = "average_monthly_debit")
    private Long averageMonthlyDebit;

    @Column(columnDefinition = "TEXT")
    private String usualTransactionPattern;
}