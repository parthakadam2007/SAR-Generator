package com.SAR_Generator.main_service.models;


import jakarta.persistence.*;
import lombok.*;

import java.math.BigDecimal;
import java.time.OffsetDateTime;
import java.util.UUID;

@Entity
@Table(name = "transactions")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Transaction {

    @Id
    @GeneratedValue
    @Column(columnDefinition = "UUID")
    private UUID id;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "case_id", nullable = false)
    private Case caseEntity;

    @Column(name = "tx_id", length = 50)
    private String txId;

    @Column(nullable = false)
    private OffsetDateTime timestamp;

    @Column(name = "from_account", length = 100)
    private String fromAccount;

    @Column(name = "to_account", length = 100)
    private String toAccount;

    @Column(precision = 15, scale = 2)
    private BigDecimal amount;

    @Column(length = 10)
    private String currency;

    @Column(length = 50)
    private String channel;

    @Column(length = 100)
    private String country;
}