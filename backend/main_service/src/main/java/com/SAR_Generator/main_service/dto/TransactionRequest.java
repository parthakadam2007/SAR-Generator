package com.SAR_Generator.main_service.dto;

import java.math.BigDecimal;
import java.time.OffsetDateTime;

import lombok.Data;

@Data
public class TransactionRequest {

    private String tx_id;
    private OffsetDateTime timestamp;
    private String from_account;
    private String to_account;
    private BigDecimal amount;
    private String currency;
    private String channel;
    private String country;
}