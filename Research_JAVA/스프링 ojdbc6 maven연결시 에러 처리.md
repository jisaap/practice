spring pom.xml

```

<!-- 오라클 ojdbc6 Maven 다운로드 용 POM.xml에서 불러올 경우 repository에서 불러올수 없는 경우 생김 -->
	<repositories>
		<repository>
			<id>codelds</id>
			<url>https://code.lds.org/nexus/content/groups/main-repo</url>
		</repository>
	</repositories>
	
	
		<dependency>
			<groupId>com.oracle</groupId>
			<artifactId>ojdbc6</artifactId>
			<version>11.2.0.3</version>
		</dependency>
		
		
		추가해주기
	

```





