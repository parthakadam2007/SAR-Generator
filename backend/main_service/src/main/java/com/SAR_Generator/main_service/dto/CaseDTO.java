package com.SAR_Generator.main_service.dto;

import lombok.*;

import java.time.OffsetDateTime;
import java.util.UUID;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class CaseDTO {

    private UUID id;

    private String caseId;

    private OffsetDateTime generatedAt;

    private String institution;

    private OffsetDateTime createdAt;
}