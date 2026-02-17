package com.SAR_Generator.main_service.dto;


import lombok.*;

import java.time.LocalDate;
import java.util.UUID;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class AccountProfileDTO {

    private UUID id;

    private UUID caseId;

    private String accountNumberMasked; // ****1234

    private String accountType;

    private LocalDate openedDate;

    private Long averageMonthlyBalance;

    private Long averageMonthlyCredit;

    private Long averageMonthlyDebit;

    private String usualTransactionPattern;
}