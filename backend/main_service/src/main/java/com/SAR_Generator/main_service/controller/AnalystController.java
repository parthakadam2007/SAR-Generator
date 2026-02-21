package com.SAR_Generator.main_service.controller;

import com.SAR_Generator.main_service.dto.AlertDTO;
import com.SAR_Generator.main_service.dto.TransactionDTO;
import com.SAR_Generator.main_service.models.Alert;

import com.SAR_Generator.main_service.services.AlertService;
import com.SAR_Generator.main_service.services.TransactionService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.UUID;

@RestController
@RequestMapping("/api/alerts")
public class AnalystController {

    private final AlertService alertService;

    private final TransactionService transactionService;

    // Constructor Injection (Best Practice)
    public AnalystController(AlertService alertService, TransactionService transactionService) {
        this.alertService = alertService;
        this.transactionService = transactionService;
    }

    @GetMapping("/transaction/{caseId}")
    public ResponseEntity<List<TransactionDTO>> getTransactions(@PathVariable UUID caseId) {
        List<TransactionDTO> transactionDTOS = transactionService.getByCaseId(caseId);
        return ResponseEntity.ok(transactionDTOS);
    }


    @GetMapping
    public ResponseEntity<List<AlertDTO>> getAllAlerts() {

        List<AlertDTO> alertDTOList = alertService.getAlerts();

        return ResponseEntity.ok(alertDTOList);
    }
}