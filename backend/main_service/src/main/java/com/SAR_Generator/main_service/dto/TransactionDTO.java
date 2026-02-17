package com.SAR_Generator.main_service.dto;


import lombok.*;

import java.math.BigDecimal;
import java.time.OffsetDateTime;
import java.util.UUID;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class TransactionDTO {

    private UUID id;

    private UUID caseId;

    private String txId;

    private OffsetDateTime timestamp;

    private String fromAccountMasked;

    private String toAccountMasked;

    private BigDecimal amount;

    private String currency;

    private String channel;

    private String country;
}