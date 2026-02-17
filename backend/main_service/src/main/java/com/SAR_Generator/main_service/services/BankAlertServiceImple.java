package com.SAR_Generator.main_service.services;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.SAR_Generator.main_service.validation.JsonValidator;


@Service
public class BankAlertServiceImple implements BankAlertService{
    @Autowired
    KafkaProducerService kafkaProducerService;

    @Autowired
    JsonValidator jsonValidator;

    @Override
    public void processAlert(String data){
        System.out.println("sending data to kafka");
        kafkaProducerService.send(data);
    }

    // @Override
    // public void saveCases(String data){
        
        
    // }
}
