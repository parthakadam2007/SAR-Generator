package com.SAR_Generator.main_service.models;


import jakarta.persistence.*;
import lombok.*;

import java.time.OffsetDateTime;
import java.util.UUID;

@Entity
@Table(
    name = "alerts",
    indexes = {
        @Index(name = "idx_alert_severity", columnList = "severity")
    }
)
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Alert {

    @Id
    @GeneratedValue
    @Column(columnDefinition = "UUID")
    private UUID id;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "case_id", nullable = false)
    private Case caseEntity;

    @Column(name = "alert_id", length = 100)
    private String alertId;

    @Column(length = 255)
    private String type;

    @Column(columnDefinition = "TEXT")
    private String description;

    @Column(name = "trigger_time")
    private OffsetDateTime triggerTime;

    @Column(length = 50)
    private String severity;
}