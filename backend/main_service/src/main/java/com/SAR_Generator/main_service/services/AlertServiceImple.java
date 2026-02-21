package com.SAR_Generator.main_service.services;

import com.SAR_Generator.main_service.dto.AlertDTO;
import com.SAR_Generator.main_service.mapper.AlertMapper;
import com.SAR_Generator.main_service.models.Alert;
import com.SAR_Generator.main_service.repository.AlertRepository;
import com.SAR_Generator.main_service.services.AlertService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
public class AlertServiceImple implements AlertService {

    @Autowired
    private AlertRepository alertRepository;

    @Autowired
    private AlertMapper alertMapper;

    @Override
    public List<AlertDTO> getAlerts() {
        //TODO : overload the function to support filert high  ,low , meduim
        try{
            // Fetch all alerts from DB
            List<Alert> alerts = alertRepository.findAll();


            // Convert Entity → DTO
            List<AlertDTO> alertDTOs = alerts.stream()
                    .map(alertMapper::toDTO)
                    .collect(Collectors.toList());

            return alertDTOs;
        }catch(Exception e){
            System.err.println("Error while fetching alerts: " + e.getMessage());

            throw new RuntimeException("Failed to fetch alerts. Please try later.");
        }
    }

}