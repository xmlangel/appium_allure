# This is a Feature file
Feature: 메인페이지

  Background:
    Given 초기화
    @JIRA-ID
    Scenario: 화면보기
        When app 클릭
        Then app 타이틀 표시
