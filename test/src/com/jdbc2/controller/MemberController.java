package com.jdbc2.controller;

import java.util.List;

import com.jdbc2.model.dao.MemberDao;
import com.jdbc2.model.vo.Member;
import com.jdbc2.view.MainView;

public class MemberController {
	private MemberDao dao=new MemberDao();
	
	public void insertMember() {
		Member m=new MainView().insertData();
		int result=dao.insertMember(m);
		String msg=result>0?"회원등록성공":"회원등록 실패";
		new MainView().printMsg(msg);
	}
	
	public void updateMember() {
		Member m = new MainView().updateData();
		int result = new MemberDao().updateMember(m);
		
		String msg =result>0?"회원정보 수정 성공":"회원정보 수정 실패";
	}
	
	public void deleteMember() {
		String id = new MainView().deleteData();
		int cheak = new MemberDao().deleteMember(id);
		new MainView().printDelete(cheak);
	}
	
	public void selectAll() {
		List<Member> list = new MemberDao().selectAll();
		new MainView().printAll(list);
	}
	
	public void selectId() {
		String id = new MainView().selectId();
		Member m = new MemberDao().selectId(id);
		new MainView().printSelectId(m);
	}
	public void selectName() {
		String name = new MainView().selectName();
		List<Member> list = new MemberDao().selectName(name);
		new MainView().printSelectName(list);
	}
	
	
	public void closePro() {
		System.exit(0);
	}
	
	
}










