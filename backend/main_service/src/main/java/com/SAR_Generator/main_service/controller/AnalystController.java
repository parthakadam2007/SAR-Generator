package com.SAR_Generator.main_service.controller;

import com.SAR_Generator.main_service.dto.AlertDTO;
import com.SAR_Generator.main_service.models.Alert;

import com.SAR_Generator.main_service.services.AlertService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

@RestController
@RequestMapping("/api/alerts")
public class AnalystController {

    private final AlertService alertService;

    // Constructor Injection (Best Practice)
    public AnalystController(AlertService alertService) {
        this.alertService = alertService;
    }


    @GetMapping
    public ResponseEntity<List<AlertDTO>> getAllAlerts() {

        List<AlertDTO> alertDTOList = alertService.getAlerts();

        return ResponseEntity.ok(alertDTOList);
    }
}