package com.jdbc2.model.dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

import com.jdbc2.model.vo.Member;

public class MemberDao {

	public Connection getConnection() {
		Connection conn=null;
		try {
			Class.forName("oracle.jdbc.driver.OracleDriver");
			conn=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe"
								,"student","student");
			conn.setAutoCommit(false);
		}catch(Exception e){
			e.printStackTrace();
		}
		return conn;
	}
	
	public int insertMember(Member m) {
		Connection conn=this.getConnection();
		Statement stmt=null;
		PreparedStatement pstmt=null;

		int result=0;
//		String sql="insert into member ~~~~";
		String sql="insert into member "
				+ "values(?,?,?,?,?,?,?,?,?,sysdate)";
		try {
//			stmt=conn.createStatement();
//			result=stmt.executeUpdate(sql);
			pstmt=conn.prepareStatement(sql);
			//pstmt.set자료형!(index,값);
			//자료형 : String,Int,Date,Double..
			//문자열 : pstmt.setString(index,값);
			//숫자형 : pstmt.setInt(index,값);
			//인덱스는 ?순으로 1번부터 자동부여
			pstmt.setString(1, m.getMemberId());
			pstmt.setString(2, m.getMemberPwd());
			pstmt.setString(3, m.getMemberName());
			pstmt.setString(4, String.valueOf(m.getGender()));
			pstmt.setInt(5, m.getAge());
			pstmt.setString(6, m.getEmail());
			pstmt.setString(7, m.getPhone());
			pstmt.setString(8, m.getAddress());
			pstmt.setString(9, m.getHobby());
			
			result=pstmt.executeUpdate();
			
		}catch(SQLException e) {
			e.printStackTrace();
		}finally {
			try {
				pstmt.close();
				if(result>0) conn.commit();
				else conn.rollback();
				conn.close();
			}catch(SQLException e) {
				e.printStackTrace();
			}
		}
		return result;
	}
	
	public int updateMember(Member m) {
		Connection conn = this.getConnection();
		PreparedStatement pstmt = null;
		int result = 0;
		String sql = "update member set "
				+ "age = ? ,"
				+ "email = ?,"
				+ "address = ?"
				+ "where member_id = ?";
		
		try {
			pstmt = conn.prepareStatement(sql);
			
			pstmt.setInt(1, m.getAge());
			pstmt.setString(2, m.getEmail());
			pstmt.setString(3, m.getAddress());
			pstmt.setString(4, m.getMemberId());
			
			result = pstmt.executeUpdate();
		}catch(SQLException e)
		{
			e.printStackTrace();
		}finally {
			try {
				if(result > 0) {
					conn.commit();
				}else {
					conn.rollback();
				}
				conn.close();
				
				
				
			}catch(SQLException s) {
				s.printStackTrace();
			}
		}
		return result;
	}
	
	public Member selectId(String id) {
		Connection conn = this.getConnection();
		Member m = new Member();
		Statement stmt = null;
		ResultSet rs = null;
		String sql = "select * from member where member_id = '"+id+"'";
		
		try {
			stmt = conn.createStatement();			
			rs = stmt.executeQuery(sql);

			if(rs.next()) {				
				m = new Member();
			m.setMemberId(rs.getString("member_id"));
			m.setMemberPwd(rs.getString("member_pwd"));
			m.setMemberName(rs.getString("member_name"));
			m.setGender(rs.getString("gender").charAt(0));
			m.setAge(rs.getInt("age"));
			m.setEmail(rs.getString("email"));
			m.setPhone(rs.getString("phone"));
			m.setAddress(rs.getString("address"));
			m.setHobby(rs.getString("hobby"));
			m.setEnrollDate(rs.getDate("enroll_date"));
			}
			
		}catch(SQLException e) {
			e.printStackTrace();
		}finally {
			try {
				conn.close();
				rs.close();
			}catch(SQLException s) {
				s.printStackTrace();
			}
		}
		return m;
	}
	
	public List<Member> selectName(String name) {
		List<Member> list = new ArrayList<Member>();
		Connection conn = this.getConnection();
		Statement stmt = null;
		ResultSet rs = null;
		String sql = "select * from member where member_name like '%"+name+"%'";
		
		try {
			stmt = conn.createStatement();
			rs = stmt.executeQuery(sql);
			
			while(rs.next()) {
				Member m = new Member();
				m.setMemberId(rs.getString("member_id"));
				m.setMemberPwd(rs.getString("member_pwd"));
				m.setMemberName(rs.getString("member_name"));
				m.setGender(rs.getString("gender").charAt(0));
				m.setAge(rs.getInt("age"));
				m.setEmail(rs.getString("email"));
				m.setPhone(rs.getString("phone"));
				m.setAddress(rs.getString("address"));
				m.setHobby(rs.getString("hobby"));
				m.setEnrollDate(rs.getDate("enroll_date"));
				
				list.add(m);
			}
		}catch(SQLException e) {
			e.printStackTrace();
		}finally {
			try {
				rs.close();
				stmt.close();
				conn.close();
			}catch(SQLException s) {
				s.printStackTrace();
			}
		}
		return list;
	}
	
	public List<Member> selectAll() {
		List<Member> list = new ArrayList<Member>();
		Connection conn = this.getConnection();
		Statement stmt = null;
		ResultSet rs = null;
		String sql = "select * from member";
		
		try {
			stmt = conn.createStatement();
			rs = stmt.executeQuery(sql);
			
			while(rs.next()) {
				Member m = new Member();
				m.setMemberId(rs.getString("member_id"));
				m.setMemberPwd(rs.getString("member_pwd"));
				m.setMemberName(rs.getString("member_name"));
				m.setGender(rs.getString("gender").charAt(0));
				m.setAge(rs.getInt("age"));
				m.setEmail(rs.getString("email"));
				m.setPhone(rs.getString("phone"));
				m.setAddress(rs.getString("address"));
				m.setHobby(rs.getString("hobby"));
				m.setEnrollDate(rs.getDate("enroll_date"));
				
				list.add(m);
			}
		}catch (SQLException e) {
			e.printStackTrace();
		} finally {
			try {
				rs.close();
				stmt.close();
				conn.close();
			}catch (SQLException s) {
				s.printStackTrace();
			}
		}
		return list;
	}
	
	public int deleteMember(String id) {
		Connection conn = this.getConnection();
		Statement stmt = null;
		int result = 0;
		String sql = "delete from member where member_id = '"+id+"'";
		
		try {
			conn.setAutoCommit(false);
			stmt = conn.createStatement();
			result = stmt.executeUpdate(sql);
		}catch ( SQLException e) {
			e.printStackTrace();
		}finally {
			try {
				if(result > 0) {
					conn.commit();
				}else {
					conn.rollback();
				}
				stmt.close();
				conn.close();
			}catch (SQLException s){
				s.printStackTrace();
			}
		}
		return result;
	}
}





