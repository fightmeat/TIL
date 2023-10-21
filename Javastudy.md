# 자바공부
1. 윈도우에 JDK 설치하기
- Eclipse 재단에서 관리하는 adoptium에 들어가서 Java 8 버전 다운로드 LTS(Long Term Support)가 붙어 있으면 오래사용할 수 있음
- Location에서 program files에서 Eclipse adoptium을 Java로 변경
- Set JAVA_HOME variable 에도 우클릭 Will be installed on local hard drive 체크
- cmd에서 java -version 하면 java 버젼을 를 확인할 수 있다.
  
2. IDE(Intergrated Development Environment) : 통합개발환경
- IntelliJ Community 설치
- 설치 체크로 path variable과 context menu Associations 체크
- Jetbrains 시작메뉴에 만든다.
- Do not import settings
- New project
- name을 JavaWorkSpace
- location을 ~\Desktop
- language = java, Build system = intelliJ, JDK = 1.8
- 만든뒤에 settingdp Editor에 General에 Mouse control

3. 자료형
- src에 new package를 chap_01을 만들고 _01_HelloWorld 생성
- chap_01에 new javaclass로 _02_DataTypes 생성
- public static void main(String[] args)을 입력하기 위해서는 psvm 또는 main 입력가능
- System.out.println(); 대신에 sout 사용가능
  
```java
package chap_01;

public class _02_DataTypes {
    public static void main(String[] args) {
        System.out.println("Hello World");
        System.out.println("안녕하세요?");
        System.out.println(12);
        System.out.println(-34);
        System.out.println(3.14);
    }
}
``` 
