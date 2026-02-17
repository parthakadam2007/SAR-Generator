package com.SAR_Generator.main_service.dto;

import lombok.*;

import java.time.OffsetDateTime;
import java.util.UUID;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class AlertDTO {

    private UUID id;

    private UUID caseId;

    private String alertId;

    private String type;

    private String description;

    private OffsetDateTime triggerTime;

    private String severity;
}