package com.SAR_Generator.main_service.mapper;

import com.SAR_Generator.main_service.dto.AlertDTO;
import com.SAR_Generator.main_service.models.Alert;
import com.SAR_Generator.main_service.models.Case;

import org.springframework.stereotype.Component;

import java.util.List;
import java.util.UUID;
import java.util.stream.Collectors;

@Component   // Makes it a Spring Bean
public class AlertMapper {

    /* =========================
       Entity → DTO
    ========================== */

    public AlertDTO toDTO(Alert alert) {

        if (alert == null) {
            return null;
        }

        return AlertDTO.builder()
                .id(alert.getId())
                .caseId(
                        alert.getCaseEntity() != null
                                ? alert.getCaseEntity().getId()
                                : null
                )
                .alertId(alert.getAlertId())
                .type(alert.getType())
                .description(alert.getDescription())
                .triggerTime(alert.getTriggerTime())
                .severity(alert.getSeverity())
                .build();
    }


    /* =========================
       DTO → Entity
    ========================== */

    public Alert toEntity(AlertDTO dto) {

        if (dto == null) {
            return null;
        }

        Case caseEntity = null;

        if (dto.getCaseId() != null) {
            caseEntity = Case.builder()
                    .id(dto.getCaseId())
                    .build();
        }

        return Alert.builder()
                .id(dto.getId()) // optional (null for new)
                .caseEntity(caseEntity)
                .alertId(dto.getAlertId())
                .type(dto.getType())
                .description(dto.getDescription())
                .triggerTime(dto.getTriggerTime())
                .severity(dto.getSeverity())
                .build();
    }


    /* =========================
       List Mapping
    ========================== */

    public List<AlertDTO> toDTOList(List<Alert> alerts) {

        return alerts.stream()
                .map(this::toDTO)
                .collect(Collectors.toList());
    }


    public List<Alert> toEntityList(List<AlertDTO> dtos) {

        return dtos.stream()
                .map(this::toEntity)
                .collect(Collectors.toList());
    }
}