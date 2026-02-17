package com.SAR_Generator.main_service.dto;

import java.time.OffsetDateTime;

import lombok.Data;

@Data
public class AlertRequest {

    private String alert_id;
    private String type;
    private String description;
    private OffsetDateTime trigger_time;
    private String severity;
}
