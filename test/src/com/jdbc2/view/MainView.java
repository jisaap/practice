package com.jdbc2.view;

import java.util.List;
import java.util.Scanner;

import com.jdbc2.controller.MemberController;
import com.jdbc2.model.vo.Member;

public class MainView {
	private MemberController controller=new MemberController();
	public void mainMenu() {
		Scanner sc=new Scanner(System.in);
		while(true) {
			System.out.println("======회원관리 프로그램 v0.2=====");
			System.out.println("1. 전체회원조회");
			System.out.println("2. 아이디로 회원조회");
			System.out.println("3. 이름으로 회원조회");
			System.out.println("4. 회원등록");
			System.out.println("5. 회원수정");
			System.out.println("6. 회원삭제");
			System.out.println("0. 종료");
			System.out.print("입력 : ");
			int cho=sc.nextInt();
			sc.nextLine();
			
			switch(cho) {
			    case 1 : controller.selectAll();break;
			    case 2 : controller.selectId();break;
			    case 3 : controller.selectName();break;
				case 4 : controller.insertMember();break;
				case 5 : controller.updateMember();break;
				case 6 : controller.deleteMember();break;
				case 0 : controller.closePro();break;
			}
		}
	}
	
	public Member insertData() {
		Scanner sc=new Scanner(System.in);
		System.out.println("====회원정보 등록====");
		System.out.print("아이디 : ");
		String id=sc.nextLine();
		System.out.print("비밀번호 : ");
		String pw=sc.nextLine();
		System.out.print("이름 : ");
		String name=sc.nextLine();
		System.out.print("성별(M/F) : ");
		String gender=sc.nextLine();
		System.out.print("나이 : ");
		int age=sc.nextInt();
		sc.nextLine();
		System.out.print("이메일 : ");
		String email=sc.nextLine();
		System.out.print("전화번호 : ");
		String phone=sc.nextLine();
		System.out.print("주소 : ");
		String address=sc.nextLine();
		System.out.print("취미(,로 구분) : ");
		String hobby=sc.nextLine();
		return new Member(id, pw, name, gender.charAt(0),
				age,email,address,phone,hobby,null);
	}
	
	public Member updateData() {
		Scanner sc = new Scanner(System.in);
		Member m = new Member();
		System.out.println("변경할 회원 아이디 입력 : ");
		m.setMemberId(sc.next());
		System.out.println("변경할 나이 입력 :");
		m.setAge(sc.nextInt());
		System.out.println("변경할 이메일 입력 :");
		m.setEmail(sc.next());
		System.out.println("변경할 주소 입력 :");
		m.setAddress(sc.next());
		return m;
	}
	
	public String selectId() {
		Scanner sc = new Scanner(System.in);
		System.out.println("검색할 아이디 입력 : ");
		return sc.nextLine();
	}
	
	public String selectName() {
		Scanner sc = new Scanner(System.in);
		System.out.println("검색할 이름 입력 : ");
		return sc.nextLine();
	}
	
	public void printSelectId(Member m) {
		System.out.println(m);
	}
	
	public String deleteData() {
		Scanner sc = new Scanner(System.in);
		System.out.println("삭제할 아이디 입력 : ");
		return sc.nextLine();
	}
	
	public void printSelectName(List<Member> list) {
		
		
		for(Member m : list) {
			System.out.println(m);
		}
	}
	
	public void printAll(List<Member> list) {
		System.out.println("======== 전체 화원 출력 ===========");
		for(Member m : list) {
			System.out.println(m);
		}
	}
	
	public void printDelete(int cheak) {
		String msg = cheak>0?"삭제가 완료되었습니다.":"삭제 실패";
       			new MainView().printMsg(msg);
	}
	
	public void printMsg(String msg) {
		System.out.println(msg);
	}
	
	
}








