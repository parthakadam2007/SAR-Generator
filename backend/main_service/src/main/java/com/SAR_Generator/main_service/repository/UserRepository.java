package com.SAR_Generator.main_service.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import com.SAR_Generator.main_service.models.User;
import java.util.UUID;

public interface UserRepository extends JpaRepository<User,UUID> {
    @Query(value = "SELECT * FROM user WHERE email = :email", nativeQuery = true)
    User findByEmailNative(String email);
}
