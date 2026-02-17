package com.SAR_Generator.main_service.services;

import java.util.List;

import org.springframework.stereotype.Service;

import com.SAR_Generator.main_service.dto.CaseFullRequestDTO;
import com.SAR_Generator.main_service.models.AccountProfile;
import com.SAR_Generator.main_service.models.Case;
import com.SAR_Generator.main_service.models.CustomerKyc;
import com.SAR_Generator.main_service.models.Transaction;
import com.SAR_Generator.main_service.repository.AccountProfileRepository;
import com.SAR_Generator.main_service.repository.AlertRepository;
import com.SAR_Generator.main_service.repository.CaseRepository;
import com.SAR_Generator.main_service.repository.CustomerKycRepository;
import com.SAR_Generator.main_service.repository.TransactionRepository;
import com.SAR_Generator.main_service.models.Alert;

import jakarta.transaction.Transactional;
import lombok.RequiredArgsConstructor;

@Service
@RequiredArgsConstructor
@Transactional   // VERY IMPORTANT
public class CaseService {

    private final CaseRepository caseRepo;
    private final CustomerKycRepository kycRepo;
    private final AccountProfileRepository accountRepo;
    private final AlertRepository alertRepo;
    private final TransactionRepository txRepo;

    public void saveFullCase(CaseFullRequestDTO dto) {

        // 1️⃣ Save Case
        Case caseEntity = Case.builder()
                .caseId(dto.getCase_id())
                .generatedAt(dto.getGenerated_at())
                .institution(dto.getInstitution())
                .build();
        System.out.println("👆"+caseEntity.getCaseId());
        caseRepo.save(caseEntity);



        // 2️⃣ Save KYC
        CustomerKyc kyc = CustomerKyc.builder()
                .caseEntity(caseEntity)
                .customerId(dto.getCustomer_kyc().getCustomer_id())
                .fullName(dto.getCustomer_kyc().getFull_name())
                .dob(dto.getCustomer_kyc().getDob())
                .pan(dto.getCustomer_kyc().getPan())
                .aadhaarLast4(dto.getCustomer_kyc().getAadhaar_last4())
                .occupation(dto.getCustomer_kyc().getOccupation())
                .declaredAnnualIncome(dto.getCustomer_kyc().getDeclared_annual_income())
                .riskCategory(dto.getCustomer_kyc().getRisk_category())
                .address(dto.getCustomer_kyc().getAddress())
                .kycLastUpdated(dto.getCustomer_kyc().getKyc_last_updated())
                .build();

        kycRepo.save(kyc);
System.out.println("👆"+caseEntity);

        // 3️⃣ Save Account
        AccountProfile acc = AccountProfile.builder()
                .caseEntity(caseEntity)
                .accountNumber(dto.getAccount_profile().getAccount_number())
                .accountType(dto.getAccount_profile().getAccount_type())
                .openedDate(dto.getAccount_profile().getOpened_date())
                .averageMonthlyBalance(dto.getAccount_profile().getAverage_monthly_balance())
                .averageMonthlyCredit(dto.getAccount_profile().getAverage_monthly_credit())
                .averageMonthlyDebit(dto.getAccount_profile().getAverage_monthly_debit())
                .usualTransactionPattern(
                        dto.getAccount_profile().getUsual_transaction_pattern()
                )
                .build();

        accountRepo.save(acc);


        // 4️⃣ Save Alerts
        if (dto.getAlerts() != null) {

            List<Alert> alerts = dto.getAlerts().stream()
                    .map(a -> Alert.builder()
                            .caseEntity(caseEntity)
                            .alertId(a.getAlert_id())
                            .type(a.getType())
                            .description(a.getDescription())
                            .triggerTime(a.getTrigger_time())
                            .severity(a.getSeverity())
                            .build())
                    .toList();

            alertRepo.saveAll(alerts);
        }


        // 5️⃣ Save Transactions
        if (dto.getTransactions() != null) {

            List<Transaction> txs = dto.getTransactions().stream()
                    .map(t -> Transaction.builder()
                            .caseEntity(caseEntity)
                            .txId(t.getTx_id())
                            .timestamp(t.getTimestamp())
                            .fromAccount(t.getFrom_account())
                            .toAccount(t.getTo_account())
                            .amount(t.getAmount())
                            .currency(t.getCurrency())
                            .channel(t.getChannel())
                            .country(t.getCountry())
                            .build())
                    .toList();

            txRepo.saveAll(txs);
        }
    }
}